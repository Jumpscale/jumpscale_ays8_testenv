from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode = "aysrepo=j.atyourservice.get('%(reponame)s', '%(repopath)s'); service=aysrepo.getService('%(role)s', '%(instance)s', reset=True); selfobj=service.actions;"






class Actions(ActionsBaseMgmt):

    def input(self,recipe,role,instance,args={}):
        if "milestone.title" not in args:
            args['milestone.title']=instance

        return args



    @action()
    def install(self):

        deadline=self.service.hrd.get("milestone.deadline")

        if deadline.startswith("+"):
            epoch=j.data.time.getEpochFuture(deadline)
            deadline=j.data.time.any2HRDateTime(int(epoch))
        else:
            deadline=j.data.time.any2HRDateTime(deadline)

        self.service.hrd.set("milestone.deadline",deadline)


        



        

    @action()
    def init(self):
        return True


    @action()
    def stop(self):
        return True


    @action()
    def start(self):
        return True


    @action()
    def monitor(self):
        return True


    @action()
    def halt(self):
        return True


    @action()
    def check_up(self):
        return True


    @action()
    def check_down(self):
        return True


    @action()
    def check_requirements(self):
        return True


    @action()
    def cleanup(self):
        return True


    @action()
    def data_export(self):
        return True


    @action()
    def data_import(self):
        return True


    @action()
    def uninstall(self):
        return True


    @action()
    def removedata(self):
        return True
