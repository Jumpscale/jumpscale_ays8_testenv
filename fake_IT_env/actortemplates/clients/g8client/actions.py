from JumpScale import j

def input(service, args={}):

    if "g8.account" not in args or args["g8.account"].strip() == "":
        args['g8.account'] = args["g8.login"]

    return args

def init(job):
    pass

def getClient(job):
    """
    return client towards g8 master
    """
    # not implemented ofcourse
    return None
