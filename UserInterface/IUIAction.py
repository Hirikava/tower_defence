import abc


class IUIAction():
    def act(self,*args):
        raise NotImplementedError