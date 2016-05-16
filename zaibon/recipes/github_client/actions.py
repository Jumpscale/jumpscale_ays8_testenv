from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode = "aysrepo=j.atyourservice.get('%(reponame)s', '%(repopath)s'); service=aysrepo.getService('%(role)s', '%(instance)s', reset=True); selfobj=service.actions;"




class Actions(ActionsBaseMgmt):


    @action()
    def install(self):
        self.monitor()


    @action()
    def monitor(self):
        g=self.getGithubClient()
        #@todo implement test

    def getGithubClient(self):
        g=j.clients.github.getClient(self.service.hrd.get("github.secret"))        
        return g

    @action()
    def test(self):
        print ("test")

    @action()
    def test2(self):
        print ("test2")        
        print ("$(github.secret)")        

    @action(queue="main")
    def testasync(self):
        print ("testasync")        
        print ("$(github.secret)")                

    def input(self,name,role,instance,serviceargs):
        return serviceargs


    @action()
    def init(self):
        return True


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
