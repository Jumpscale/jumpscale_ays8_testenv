from JumpScale import j


class Actions():

    def input(self, service, args={}):

        if "g8.account" not in args or args["g8.account"].strip() == "":
            args['g8.account'] = args["g8.login"]

        return args

    def init(self, job):
        pass

    def getClient(self, job):
        """
        return client towards g8 master
        """
        # not implemented ofcourse
        return None
