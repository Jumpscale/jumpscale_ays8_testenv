from JumpScale import j


class Actions(ActionsBaseMgmt):

    def init(self, service):
        '''
        STEPS
        - init app.docker, parent is parent os of docker_g8_controller: this will make sure we have a proper docker
        - 
        '''

    def install(self, service):
        '''

        '''
        self.stop()
        #@todo pull appropriate controller docker
        #@todo configure weave
        self.start()
        if self.monitor()==False:
            ...
        return True

    def start(self, service):
        pass

    def stop(self, service):
        '''
        stop the docker which optionally is running
        '''
        pass

    def monitor(self, service):
        '''
        - ping os in docker
        - ssh os in docker
        - 
        '''
