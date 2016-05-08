from JumpScale import j


class Actions(ActionsBaseMgmt):

    def getSSHKey(self):
        return "someprivkey", "somepubkey"

    def _startAgent(self):
        # FIXME
        j.do.execute("ssh-agent", die=False, showout=False, outputStderr=False)

    def init(self):
        """
        create key
        """
        if self.service.hrd.get("key.name") == "":
            self.service.hrd.set("key.name", self.service.instance)

        name=self.service.hrd.get("key.name") 
        
        tmpdir=j.sal.fs.getTmpDirPath()

        if j.do.getSSHKeyPathFromAgent(name, die=False)!=None:
            keyfile = j.do.getSSHKeyPathFromAgent(name)
        elif self.service.hrd.get("key.path") != "":
            keyfile = self.service.hrd.get("key.path")
        else:
            keyfile=j.sal.fs.joinPaths(tmpdir,name)

        keydest = j.sal.fs.joinPaths(self.service.path, "sshkey_%s"%self.service.instance)

        self.service.hrd.set('key.pub', "somepubkey")
        self.service.hrd.set('key.priv', "someprivkey")

        self.install()


    def install(self):
        # j.do.loadSSHAgent()
        self.start()


    def start(self):
        """
        Add key to SSH Agent if not already loaded
        """
        keypath=j.sal.fs.joinPaths(self.service.path, "sshkey_%s"%self.service.instance)
        # j.do.loadSSHKeys(keypath)
        return True


    #not sure we can remove, key can be used for something else
    # def stop(self):
    #     """
    #     Remove key from SSH Agent
    #     """
    #     keyfile = self._getKeyPath()
    #     if j.do.getSSHKeyPathFromAgent('$(key.name)', die=False) is not None:
    #         keyloc = "/root/.ssh/%s" % '$(key.name)'
    #         cmd = 'ssh-add -d %s' % keyfile
    #         j.do.executeInteractive(cmd)



