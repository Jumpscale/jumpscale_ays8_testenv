from JumpScale import j


class Actions():

    def getMachine(self, job):
        machine=None
        return machine

    def open_port(self, requested_port, public_port=None):
        """
        Open port in the firewall by creating port forward
        if public_port is None, auto select available port
        Return the public port assigned
        """
        pf = service.hrd.getList('portforwards', [])
        pf.append("%s:%s" % (spaceport, requested_port))
        service.hrd.set('portforwards', pf)
        return spaceport

    def install(self, job):
        
        machineid=service.hrd.getSet('machineid', j.data.idgenerator.generateRandomInt(10,20))

        if not service.hrd.get('publicip', ''):
            service.hrd.set('publicip', "212.3.45.%"%j.data.idgenerator.generateRandomInt(70,120))
            service.hrd.set('sshport', executor.port)

        for child in service.children:
            child.hrd.set("ssh.addr", service.hrd.get("publicip"))
            child.hrd.set("ssh.port", service.hrd.get("sshport"))

        for port in service.hrd.getList('ports'):
            ss = port.split(':')
            if len(ss) == 2:
                service.actions.open_port(requested_port=ss[1], public_port=ss[0])
            else:
                service.actions.open_port(requested_port=port)


    def uninstall(self, job):
        pass
        