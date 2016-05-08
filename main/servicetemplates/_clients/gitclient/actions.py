from JumpScale import j


class Actions():

    def init(self):
        return True

    def install(self):
        self.service.logger.info("Installed ok:%s"%self.service)
        return True
