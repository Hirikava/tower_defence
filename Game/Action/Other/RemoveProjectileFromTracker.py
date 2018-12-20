from Game.Action.Infrastructer.IGameAction import IGameAction


class RemoveProjectileFromTracker(IGameAction):
    def __init__(self,target):
        self.__target__ = target

    def act(self,*args):
        args[5].remove(self.__target__)
