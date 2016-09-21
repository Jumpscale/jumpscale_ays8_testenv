

class Actions():

    def init(self, job):
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

    def getExecutor(self, job):
        return j.tools.executor.getLocal()

    def monitor(self, job):
        return True

    def install(self, job):
        if 'sshkey' in service.producers:
            sshkey = service.producers['sshkey'][0]
            sshkey_pub = sshkey.hrd.get('key.pub')
        else:
            raise RuntimeError("No sshkey found. please consume an sshkey service")

        print("authorize ssh key to machine")


    def consume(self, job):
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
            
        