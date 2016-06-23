from JumpScale import j


class Actions(ActionsBaseMgmt):
    def install(self, service):
        '''        
        #@todo
        - make sure docker is properly installed (use cuisine functionality)
        '''
        raise RuntimeError("error")
        return True

    def start(self, service):
        return True

    def stop(self, service):
        '''
        @todo stop all docker instances
        '''

    def monitor(self, service):
        '''
        @todo monitor that docker is properly working
        '''
