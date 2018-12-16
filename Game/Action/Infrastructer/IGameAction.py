import abc
from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder

class IGameAction(IGameActionHolder):
    @abc.abstractmethod
    def act(self,*args):
        raise NotImplementedError

    def get_actions(self):
        return [self]