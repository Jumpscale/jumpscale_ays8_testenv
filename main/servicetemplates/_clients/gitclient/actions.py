from JumpScale import j


class Actions(ActionsBaseMgmt):

    def init(self):
        return True

    def install(self):
        self.service.logger.info("Installed ok:%s"%self.service)
        return True
