from JumpScale import j


class Actions(ActionsBaseMgmt):

    @action()
    def process(self):
        Issue = j.clients.github.getIssueClass()
        repo = self.service.parent.actions.get_github_repo()

        # only process this specific issue.
        for issue in repo.issues:
            if issue.id == self.service.model['id']:
                repo.process_issues([issue])
                break

    @action()
    def getIssueFromGithub(self):

        repo=self.service.actions.get_github_repo()

        path=j.sal.fs.joinPaths(self.service.path,"issue.yaml")

        j.sal.fs.writeFile(path,str(md))
