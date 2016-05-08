from JumpScale import j

ActionsBase = self.service.aysrepo.getActionsBaseClassMgmt()


class Actions(ActionsBase):

    def __init__(self, service):
        super(Actions, self).__init__(service)
        self._cuisine = None

    @property
    def cuisine(self):
        #not implemented
        return None

    def hrd(self):
        # def setDockerSize():
        #     size = self.service.hrd.getInt("docker.size")
        #     ok = [8]
        #     for item in ok:
        #         if item == size:
        #             self.service.hrd.set("docker.size", item)
        #             return
        #         if size < item:
        #             self.service.hrd.set("docker.size", item)
        #             return
        #     self.service.hrd.set("docker.size", item)

        def setDiskSize():
            size = self.service.hrd.getInt("disk.size")
            ok = [20]
            for item in ok:
                if item == size:
                    self.service.hrd.set("disk.size", item)
                    return
                if size < item:
                    self.service.hrd.set("disk.size", item)
                    return
            self.service.hrd.set("disk.size", item)

        # setDockerSize()
        setDiskSize()

    def getClient(self):
        vdc = self.service.parent
        client = vdc.action_methods_mgmt.getClient()
        return client

    def getSpace(self):
        vdc = self.service.parent
        farm = vdc.parent

        account = self.getClient().account_get(farm.hrd.get('account'))
        space = account.space_get(vdc.instance, location=vdc.hrd.get('location'))
        return space

    def getMachine(self):
        # space = self.getSpace()

        # if self.service.instance in space.machines:
        #     machine = space.machines[self.service.instance]
        # else:
        #     machine = space.machine_create(name=self.service.instance,
        #                                    image='$(os.image)',
        #                                    memsize=int('$(os.size)'))
        machine=None
        return machine

    def install(self):
        # executor = machine.get_ssh_connection()

        self.service.hrd.set("machine.id", j.data.idgenerator.generateRandomInt(10,20))
        self.service.hrd.set("machine.publicip", "212.3.44.%"%j.data.idgenerator.generateRandomInt(70,120))
        self.service.hrd.set("machine.privateip", "192.168.10.%"%j.data.idgenerator.generateRandomInt(70,120))
        self.service.hrd.set("machine.sshport", j.data.idgenerator.generateRandomInt(2022,2080))

        # authorize sshkey for root user
        # executor.cuisine.set_sudomode()
        if 'sshkey' in self.service.producers:
            sshkey = self.service.producers['sshkey'][0]
            sshkey_pub = sshkey.hrd.get('key.pub')
        else:
            raise RuntimeError("No sshkey found. please consume an sshkey service")
        self.service.logger.info("authorize ssh key to machine")
        # executor.cuisine.ssh.authorize('root', sshkey_pub)


    def uninstall(self):
        self.service.logger.info("UNINSTALL OK")
        return True
