from JumpScale import j


class Actions():

    def init(self, job):
        '''
        STEPS
        - init app.docker, parent is parent os of docker_g8_controller: this will make sure we have a proper docker
        - 
        '''

    def install(self, job):
        '''

        '''
        self.stop()
        #@todo pull appropriate controller docker
        #@todo configure weave
        self.start()
        if self.monitor()==False:
            ...
        return True

    def start(self, job):
        pass

    def stop(self, job):
        '''
        stop the docker which optionally is running
        '''
        pass

    def monitor(self, job):
        '''
        - ping os in docker
        - ssh os in docker
        - 
        '''
