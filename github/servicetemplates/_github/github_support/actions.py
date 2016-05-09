from JumpScale import j


class Actions(ActionsBaseMgmt):

    @action()
    def from_github_ticket(self):
        for key, v in j.core.db.hgetall('webhooks').items():
            if not key.decode().startswith('issues.'):
                continue

            try:
                data = j.data.serializer.json.loads(v.decode())
            except:
                print("bad formated data for key %s" % key)
                continue

            account = data['repository']['owner']['login']
            name = data['repository']['name']

            repo_service = None
            for s in self.service.producers['github_repo']:
                if name == s.hrd.getStr('repo.name') and account == s.hrd.getStr('repo.account'):
                    repo_service = s
                    break

            if repo_service is None:
                print("targeted repo is not monitored by this service.")
                # TODO, send email back to client to tell him
                continue

            repo = repo_service.actions.get_github_repo()
            issue = repo.getIssue(data['issue']['number'])
            if issue.body.startswith('Ticket_'):
                # already processed
                # delete issue from redis
                j.core.db.hdel('webhooks', key)
                continue

            # allocation of a unique ID to the Ticket
            guid = j.data.idgenerator.generateGUID()
            # Add ticket id in issue description
            issue.body = "Ticket_%s\n\n%s" % (guid, issue.body)
            # add labels to issue
            labels = issue.labels.copy()
            if 'assistance request' not in labels:
                labels.append('assistance request')
                issue.labels = labels
            # creation of the issue in the github repo
            repo.issues.append(issue)
            # Create issue service instance of the newly created github issue
            args = {'github.repo': repo_service.instance}
            service = self.service.aysrepo.new(name='github_issue', instance=str(issue.id), args=args, model=issue.ddict)

            # delete issue from redis when processed
            j.core.db.hdel('webhooks', key)



    @action()
    def from_email_ticket(self, event):
        email = j.data.models.cockpit_event.Email.from_json(event)

        if not email.subject.startswith('(Ticket)'):
            # this mail doesn't concerne us
            return

        # find for which repo is targeted by this email
        repo_name = ''
        for l in email.body.splitlines():
            if l.startswith("repository:"):
                repo_name = l[len("repository:"):].strip()
                break
            elif l.startswith("repo:"):
                repo_name = l[len("repo:"):].strip()
                break

        if repo_name == '':
            print("can't identify targeted repository")
            # TODO, send email back to client to tell him
            return

        repo_service = None
        for s in self.service.producers['github_repo']:
            if repo_name == s.hrd.getStr('repo.name'):
                repo_service = s
                break

        if repo_service is None:
            print("targeted repo is not monitored by this service.")
            # TODO, send email back to client to tell him
            return

        Issue = j.clients.github.getIssueClass()
        repo = repo_service.actions.get_github_repo()
        # allocation of a unique ID to the Ticket
        guid = j.data.idgenerator.generateGUID()
        # Add ticket id in issue description
        body = "Ticket_%s\n\n" % guid
        body += email.body
        # creation of the issue in the github repo
        issue_obj = repo.api.create_issue(email.subject, body=body, labels=['assistance request'])
        issue = Issue(repo=repo, githubObj=issue_obj)
        repo.issues.append(issue)
        # Create issue service instance of the newly created github issue
        args = {'github.repo': repo_service.instance}
        service = self.service.aysrepo.new(name='github_issue', instance=str(issue.id), args=args, model=issue.ddict)
