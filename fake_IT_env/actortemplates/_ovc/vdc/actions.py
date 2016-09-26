
from JumpScale import j




    def init( job):

        clientaysi = service.getProducers("g8client")[0]

        if service.hrd.get("g8.account") == "":
            service.hrd.set("g8.account", clientaysi.hrd.get("g8.login"))

        if service.hrd.get("g8.location") == "":
            service.hrd.set('g8.location', "alocation%s"%j.data.idgenerator.generateRandomInt(10,20))

    def install( job):
        acc = client.account_get(service.hrd.get('g8.account'))
        # space = acc.space_get("$(service.instance)", service.hrd.get('g8.location'))

    def uninstall( job):
        return True

    def getClient( job):
        clientname = """$(producer.g8client)"""
        clientname = clientname.strip().strip("',")
        return clientname
