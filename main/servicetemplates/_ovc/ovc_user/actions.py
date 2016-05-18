
from JumpScale import j


class Actions(ActionsBaseMgmt):

    def init(self, service):
        pass

    def install(self, service):
        return True

    def uninstall(self, service):
        return True

    def getClient(self, service):
        return None
