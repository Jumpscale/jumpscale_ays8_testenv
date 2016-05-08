from JumpScale import j


class Actions():

    def getMachine(self):
        machine=None
        return machine

    def open_port(self, requested_port, public_port=None):
        """
        Open port in the firewall by creating port forward
        if public_port is None, auto select available port
        Return the public port assigned
        """
        pf = self.service.hrd.getList('portforwards', [])
        pf.append("%s:%s" % (spaceport, requested_port))
        self.service.hrd.set('portforwards', pf)
        return spaceport

    def install(self):
        
        machineid=self.service.hrd.getSet('machineid', j.data.idgenerator.generateRandomInt(10,20))

        if not self.service.hrd.get('publicip', ''):
            self.service.hrd.set('publicip', "212.3.45.%"%j.data.idgenerator.generateRandomInt(70,120))
            self.service.hrd.set('sshport', executor.port)

        for child in self.service.children:
            child.hrd.set("ssh.addr", self.service.hrd.get("publicip"))
            child.hrd.set("ssh.port", self.service.hrd.get("sshport"))

        for port in self.service.hrd.getList('ports'):
            ss = port.split(':')
            if len(ss) == 2:
                self.service.actions.open_port(requested_port=ss[1], public_port=ss[0])
            else:
                self.service.actions.open_port(requested_port=port)


    def uninstall(self):
        pass
        