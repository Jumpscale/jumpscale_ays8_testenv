from JumpScale import j


class Actions(ActionsBaseMgmt):


    def input(self,name,role,instance,args={}):

        if "g8.account" not in args or args["g8.account"].strip()=="":
            args['g8.account']=args["g8.login"]

        return args


    def init(self, service):
        pass

    def getClient(self, service):
        """
        return client towards g8 master
        """
        #not implemented ofcourse
        return None
