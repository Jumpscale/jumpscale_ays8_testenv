from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)






class Actions(ActionsBaseMgmt):

    def getSSHKey(self, service):
        return "someprivkey", "somepubkey"

    def _startAgent(self, service):
        # FIXME
        j.do.execute("ssh-agent", die=False, showout=False, outputStderr=False)


    @action()
    def init(self, service):
        """ # testing changing the template
        create key
        """
        if service.hrd.get("key.name") == "":
            service.hrd.set("key.name", service.instance)

        name=service.hrd.get("key.name") 
        
        tmpdir=j.sal.fs.getTmpDirPath()

        if j.do.getSSHKeyPathFromAgent(name, die=False)!=None:
            keyfile = j.do.getSSHKeyPathFromAgent(name)
        elif service.hrd.get("key.path") != "":
            keyfile = service.hrd.get("key.path")
        else:
            keyfile=j.sal.fs.joinPaths(tmpdir,name)

        keydest = j.sal.fs.joinPaths(service.path, "sshkey_%s"%service.instance)

        service.hrd.set('key.pub', "somepubkey")
        service.hrd.set('key.priv', "someprivkey")




    @action()
    def install(self, service):
        # j.do.loadSSHAgent()
        pass



    @action()
    def start(self, service):
        """
        Add key to SSH Agent if not already loaded
        """
        keypath=j.sal.fs.joinPaths(service.path, "sshkey_%s"%service.instance)
        # j.do.loadSSHKeys(keypath)
        return True


    #not sure we can remove, key can be used for something else
    # def stop(self, service):
    #     """
    #     Remove key from SSH Agent
    #     """
    #     keyfile = self._getKeyPath()
    #     if j.do.getSSHKeyPathFromAgent('$(key.name)', die=False) is not None:
    #         keyloc = "/root/.ssh/%s" % '$(key.name)'
    #         cmd = 'ssh-add -d %s' % keyfile
    #         j.do.executeInteractive(cmd)



    def input(self, service, name, role, instance, serviceargs):
        return serviceargs


    @action()
    def stop(self, service):
        return True


    @action()
    def monitor(self, service):
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


    @action()
    def consume(self, service):
        return True
