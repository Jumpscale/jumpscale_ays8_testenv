from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode = "aysrepo=j.atyourservice.get('%(reponame)s', '%(repopath)s'); service=aysrepo.getService('%(role)s', '%(instance)s', reset=True); selfobj=service.actions;"






class Actions(ActionsBaseMgmt):


    def input(self,name,role,instance,args={}):

        #if repo.name not filled in then same as instance
        if "repo.name" not in args or args["repo.name"].strip()=="":
            args["repo.name"]=instance

        cats={}
        #check milestone membership
        import ipdb; ipdb.set_trace()
        for aysi in self.service.aysrepo.findServices(role="github_milestone"):
            categories=aysi.hrd.getList("milestone.category")
            for cat in categories:
                if cat not in cats:
                    cats[cat]=[]
                if aysi not in cats[cat]:
                    cats[cat].append(aysi)


        if 'milestone.category' in args:

            args["milestones"]=[]

            catsToFillIn=args['milestone.category']
            if not j.data.types.list.check(catsToFillIn):
                if catsToFillIn.find(",")!=-1:
                    catsToFillIn=[item for item in catsToFillIn.split(",") if item.strip()!=""]
                else:
                    catsToFillIn=[catsToFillIn]

            for catToFillIn in catsToFillIn:
                if catToFillIn in cats:
                    for ays_repo in cats[catToFillIn]:
                        args["milestones"].append(ays_repo.instance)        

        if "milestones" in args:
            args["milestones"].sort()

        return args

    @action()   
    def init(self):

        #set url based on properties of parent
        url=self.service.parent.hrd.get("github.url").rstrip("/")
        url+="/%s"%self.service.hrd.get("repo.name")
        self.service.hrd.set("repo.url",url)

        #set path based on properties from above

        import ipdb; ipdb.set_trace()
        clienthrd=self.service.producers["github_client"][0].hrd

        clienthrd.set("code.path",j.dirs.replaceTxtDirVars(clienthrd.get("code.path")))

        path=j.sal.fs.joinPaths(clienthrd.get("code.path"),self.service.hrd.get("repo.account"),self.service.hrd.get("repo.name"))

        self.service.hrd.set("code.path",path)
        
        return True


    @action()
    def install(self):
        # self.service.actions.pull()
        self.service.actions.getIssuesFromGithub()
        self.service.actions.setMilestonesOnGithub()

    @action()   
    def pull(self):
        j.do.pullGitRepo(url=self.service.hrd.get("repo.url"), dest= self.service.hrd.get("code.path"), login=None, passwd=None, depth=1, \
            ignorelocalchanges=False, reset=False, branch=None, revision=None, ssh=True, executor=None, codeDir=None)

    @action()
    def setMilestonesOnGithub(self):

        repo=self.service.actions.get_github_repo()

        if repo.type in ["proj","org"]:            
            milestonesSet=[]
            for service in self.service.getProducers("github_milestone"):
                title=service.hrd.get("milestone.title")
                description=service.hrd.get("milestone.description")
                deadline=service.hrd.get("milestone.deadline")
                owner=service.hrd.get("milestone.owner")
                name=service.instance

                repo.createMilestone(name,title,description,deadline,owner)

                milestonesSet.append(name)

            # for name in repo.milestoneNames:
            #     if name not in milestonesSet:
            #         repo.deleteMilestone(name)
        else:
            if repo.type not in ["code"]:
                for name in repo.milestoneNames:
                    # repo.deleteMilestone(name)
                    print ("DELETE MILESTONE:%s %s"%(repo,name))

    # def getIssuesFromAYS(self):

    #     client=self.service.getProducers('github_client')[0].actions.getGithubClient()
    #     repokey=self.service.hrd.get("repo.account")+"/"+self.service.hrd.get("repo.name")
    #     repo=client.getRepo(repokey)

    #     path=j.sal.fs.joinPaths(self.service.path,"issues.md")
    #     content=j.sal.fs.fileGetContents(path)

    #     md=j.data.markdown.getDocument(content)    

    #     issueblock=""        
    #     state="start"
    #     issueNumber=0
    #     for item in md.items:
    #         print(item.type)

    #         if item.type=="comment1line": 
    #             if issueNumber!=0:
    #                 #process previously gathered issue
    #                 issue=repo.getIssueFromMarkdown(issueNumber,issueblock)

    #             issueblock=""
    #             state="block"
    #             issueNumber=j.data.tags.getObject(item.text).tagGet("issue")                   
    #             continue

    #         if state=="block":
    #             issueblock+=str(item)+"\n"   

    #     if issueNumber!=0:
    #         repo.getIssueFromMarkdown(issueNumber,issueblock)

    #     repo.issues_loaded=True

    #     return repo
        
    def get_github_repo(self):
        client=self.service.getProducers('github_client')[0].actions.getGithubClient()
        repokey=self.service.hrd.get("repo.account")+"/"+self.service.hrd.get("repo.name")
        repo=client.getRepo(repokey)
        fromAys=True
        if self.service.state.get("getIssuesFromGithub")!="OK":
            #means have not been able to get the issues from github properly, so do again
            fromAys=False
        if repo.issues_loaded==False:            
            if fromAys:
                print ("LOAD ISSUES FROM AYS")
                # self.service.state.set("getIssuesFromAYS","DO")
                self.service.actions.getIssuesFromAYS()
                repo.issues_loaded=True
            else:
                from IPython import embed
                print ("DEBUG NOW issues loaded false,LOAD ISSUES FROM GITHUB")
                embed()
                ppp
                print ("LOAD ISSUES FROM GITHUB")
                # self.service.state.set("getIssuesFromGithub","DO")
                self.service.actions.getIssuesFromGithub(force=True)   
                repo.issues_loaded=True
        return repo

    @action()
    def processIssues(self):       
        repo=self.service.actions.get_github_repo()
        repo.process_issues()

    def stories2pdf(self):
        repo=self.service.actions.get_github_repo()
        from IPython import embed
        print ("DEBUG NOW stories 2 pdf")
        embed()

    @action()  
    def test(self):
        print ("TEST")
        
    @action()        
    def getIssuesFromGithub(self):
        config=self.service.getProducers('github_config')[0]

        projtype=self.service.hrd.get("repo.type")
        labels=[]

        for key, value in config.hrd.getDictFromPrefix("github.label").items():
            # label=key.split(".")[-1]
            label=key.replace(".","_")
            if projtype in value or "*" in value:
                labels.append(label)   

        client=self.service.getProducers('github_client')[0].actions.getGithubClient()

        reponame="$(repo.account)/$(repo.name)"
        r=client.getRepo(reponame)

        #first make sure issues get right labels
        r.labels=labels

        labelsprint=",".join(labels)

        self.service.logger.info ("Have set labels in %s:%s"%(self.service,labelsprint))

        issues=r.loadIssues()

        if issues!=[]:

            from IPython import embed
            print ("DEBUG NOW getIssuesFromGithub")
            embed()
            p
        

        # path=j.sal.fs.joinPaths(self.service.path,"issues.md")
        # r.serialize2Markdown(path)

        self.service.state.set("getIssuesFromGithub","OK")
        self.service.state.save()

        r.issues_loaded=True

        self.service.actions.processIssues(force=True)




    # def change(self,stateitem):
    #     if stateitem.name not in ["install"]:
    #         stateitemToChange=self.service.state.getSet("install")
    #         if stateitemToChange.state=="OK":
    #             stateitemToChange.state="CHANGED"
    #             self.service.state.save()



        

    @action()
    def stop(self):
        return True


    @action()
    def start(self):
        return True


    @action()
    def monitor(self):
        return True


    @action()
    def halt(self):
        return True


    @action()
    def check_up(self):
        return True


    @action()
    def check_down(self):
        return True


    @action()
    def check_requirements(self):
        return True


    @action()
    def cleanup(self):
        return True


    @action()
    def data_export(self):
        return True


    @action()
    def data_import(self):
        return True


    @action()
    def uninstall(self):
        return True


    @action()
    def removedata(self):
        return True