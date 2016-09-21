from JumpScale import j


class Actions():
    def install(self, job):
        '''        
        #@todo
        - make sure docker is properly installed (use cuisine functionality)
        '''
        raise RuntimeError("error")
        return True

    def start(self, job):
        return True

    def stop(self, job):
        '''
        @todo stop all docker instances
        '''

    def monitor(self, job):
        '''
        @todo monitor that docker is properly working
        '''
