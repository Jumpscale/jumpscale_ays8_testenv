
from JumpScale import j


class Actions(ActionsBaseMgmt):

    def init(self, service):
        '''
        STEPS
        - find the 3 controllers, there need to be 3, do error otherwise
        - for each controller create
           - docker.g8.controller (consume the os.ssh) as children

        '''

    def install(self, service):
        '''
        call the monitor step, make sure it worked
        '''


    def monitor(self, service):
        '''
        '''
        #nothing yet, will do later
        return True