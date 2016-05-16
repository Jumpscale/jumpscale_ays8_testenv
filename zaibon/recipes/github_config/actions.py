from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode = "aysrepo=j.atyourservice.get('%(reponame)s', '%(repopath)s'); service=aysrepo.getService('%(role)s', '%(instance)s', reset=True); selfobj=service.actions;"







class Actions(ActionsBaseMgmt):

    

    @action()
    def init(self):

        config="""
        github.label.priority.critical: ['*']
        github.label.priority.minor: ['*']
        github.label.priority.normal: ['*']
        github.label.priority.urgent: ['*']
        github.label.process.duplicate: ['*']
        github.label.process.wontfix: ['*']
        github.label.state.inprogress: ['*']
        github.label.state.question: ['*']
        github.label.state.verification: ['*']
        github.label.type.bug: [code, ays, cockpit, doc, www]
        github.label.type.feature: [code, ays, cockpit, doc, www]
        github.label.type.monitor: [proj, www, cockpit]
        github.label.type.question: [home, code, proj, ays, doc, cockpit, www,milestone,org]
        github.label.type.story: [home, proj, milestone,org]
        github.label.type.task: [home,milestone,proj,org]
        github.label.type.ticket: [proj,org]
        github.label.type.lead: [proj,org]
        github.project.types: [home, proj, cockpit, doc, ays, code, www, milestone,org]
        """


        j.data.text.strip(config)

        labels=j.data.serializer.yaml.loads(config)

        self.service.hrdCreate()
        self.service.hrd.setArgs(labels)

    def getGithubClient(self):        
        from github import Github
        g=Github("$(github.secret)")
        return g



    @action()
    def install(self):
        #test
        self.monitor()


    @action()
    def monitor(self):
        g=self.getGithubClient()
    

    def input(self,name,role,instance,serviceargs):
        return serviceargs


    @action()
    def stop(self):
        return True


    @action()
    def start(self):
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
