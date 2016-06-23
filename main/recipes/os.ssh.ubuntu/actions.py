from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)





class Actions(ActionsBaseMgmt):


    @action()
    def init(self, service):
        if service.hrd.getBool('aysfs', False):
            service.aysrepo.new('aysfs', args={'os': service.instance}, parent=service)

        # if weave:
        #     instantiate weave
        # if agent:
        #     instantiate agent
        # sshkey = service.aysrepo.getService(role='sshkey', instance=service.hrd.getStr('sshkey'))
        # service.hrd.set("ssh.key.public", sshkey.hrd.get("key.pub"))
        # service.hrd.set("ssh.key.private", sshkey.hrd.get("key.priv"))

        # if service.hrd.get("system.backdoor.passwd").strip() == "":
        #     service.hrd.set("system.backdoor.passwd", j.data.idgenerator.generateXCharID(12))
        return True

    def getExecutor(self, service):
        return j.tools.executor.getLocal()


    @action()
    def monitor(self, service):
        return True


    @action()
    def install(self, service):
        if 'sshkey' in service.producers:
            sshkey = service.producers['sshkey'][0]
            sshkey_pub = sshkey.hrd.get('key.pub')
        else:
            raise RuntimeError("No sshkey found. please consume an sshkey service")

        print("authorize ssh key to machine")



    @action()
    def consume(self, service):
        print ('consuming!')

        # if service.parent.hrd.get("type","")=="develop":

        #     from IPython import embed
        #     print ("DEBUG NOW wipe machine!!!")
        #     embed()
        #     p
        # else:
        #     from IPython import embed
        #     print ("DEBUG NOW cssh.ubuntu")
        #     embed()
        #     p
            
        

    def input(self, service, name, role, instance, serviceargs):
        return serviceargs


    @action()
    def stop(self, service):
        return True


    @action()
    def start(self, service):
        return True


    @action()
    def halt(self, service):
        return True


    @action()
    def check_up(self, service):
        return True


    @action()
    def check_down(self, service):
        return True


    @action()
    def check_requirements(self, service):
        return True


    @action()
    def cleanup(self, service):
        return True


    @action()
    def data_export(self, service):
        return True


    @action()
    def data_import(self, service):
        return True


    @action()
    def uninstall(self, service):
        return True


    @action()
    def removedata(self, service):
        return True
