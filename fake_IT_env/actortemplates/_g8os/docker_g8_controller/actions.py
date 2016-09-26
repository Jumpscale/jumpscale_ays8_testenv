from JumpScale import j




def init( job):
    '''
    STEPS
    - init app.docker, parent is parent os of docker_g8_controller: this will make sure we have a proper docker
    -
    '''

def install( job):
    '''

    '''
    self.stop()
    #@todo pull appropriate controller docker
    #@todo configure weave
    self.start()
    if self.monitor()==False:
        ...
    return True

def start( job):
    pass

def stop( job):
    '''
    stop the docker which optionally is running
    '''
    pass

def monitor( job):
    '''
    - ping os in docker
    - ssh os in docker
    -
    '''
