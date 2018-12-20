import abc

class IGraphicsAction():
    @abc.abstractmethod
    def act(self,*args):
        raise NotImplementedError