# fake example



def input( job):
    return job.model.args

def init( job):
    print("INIT OF DATACENTER")
    return True

def install( job):
    '''
    #@todo
    '''
    raise RuntimeError("error")
    return True

def start( job):
    return True

def stop( job):
    '''
    @todo stop all docker instances
    '''

def monitor( job):
    '''
    @todo monitor that docker is properly working
    '''
