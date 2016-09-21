# fake example


class Actions():

    def input(self, job):
        return job.model.args

    def init(self, job):
        return True

    def install(self, job):
        '''
        #@todo
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
