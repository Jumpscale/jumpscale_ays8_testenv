from JumpScale import j


class Actions():

    def init(self, service):
        return True

    def install(self, service):
        self.monitor()

    def monitor(self, service):
        g=self.getGithubClient()
        #@todo implement test

    def getGithubClient(self, service):
        g=j.clients.github.getClient("$(github.secret)")
        return g
