
from JumpScale import j


class Actions():

    def init(self):

        clientaysi = self.service.getProducers("g8client")[0]

        if self.service.hrd.get("g8.account") == "":
            self.service.hrd.set("g8.account", clientaysi.hrd.get("g8.login"))

        if self.service.hrd.get("g8.location") == "":
            self.service.hrd.set('g8.location', "alocation%s"%j.data.idgenerator.generateRandomInt(10,20))

    def install(self):
        acc = client.account_get(self.service.hrd.get('g8.account'))
        # space = acc.space_get("$(service.instance)", self.service.hrd.get('g8.location'))

    def uninstall(self):
        return True

    def getClient(self):
        clientname = """$(producer.g8client)"""
        clientname = clientname.strip().strip("',")
        return clientname
