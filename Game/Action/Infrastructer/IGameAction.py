import abc

class IGameAction():
    @abc.abstractmethod
    def act(self,*args):
        raise NotImplementedError