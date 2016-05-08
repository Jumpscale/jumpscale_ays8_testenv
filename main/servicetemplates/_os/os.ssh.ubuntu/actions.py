

class Actions(ActionsBaseMgmt):

    def init(self):
        if self.service.hrd.getBool('aysfs', False):
            self.service.aysrepo.new('aysfs', args={'os': self.service.instance}, parent=self.service)

        # if weave:
        #     instantiate weave
        # if agent:
        #     instantiate agent
        # sshkey = self.service.aysrepo.getService(role='sshkey', instance=self.service.hrd.getStr('sshkey'))
        # self.service.hrd.set("ssh.key.public", sshkey.hrd.get("key.pub"))
        # self.service.hrd.set("ssh.key.private", sshkey.hrd.get("key.priv"))

        # if self.service.hrd.get("system.backdoor.passwd").strip() == "":
        #     self.service.hrd.set("system.backdoor.passwd", j.data.idgenerator.generateXCharID(12))
        return True

    def getExecutor(self):
        return None

    def monitor(self):
        return True

    def install(self):
        if 'sshkey' in self.service.producers:
            sshkey = self.service.producers['sshkey'][0]
            sshkey_pub = sshkey.hrd.get('key.pub')
        else:
            raise RuntimeError("No sshkey found. please consume an sshkey service")

        print("authorize ssh key to machine")

        # if self.service.parent.hrd.get("type","")=="develop":

        #     from IPython import embed
        #     print ("DEBUG NOW wipe machine!!!")
        #     embed()
        #     p
        # else:
        #     from IPython import embed
        #     print ("DEBUG NOW cssh.ubuntu")
        #     embed()
        #     p
            
        
