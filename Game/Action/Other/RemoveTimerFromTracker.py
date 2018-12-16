from Game.Action.Infrastructer.IGameAction import IGameAction


class RemoveTimerFromTracker(IGameAction):
    def __init__(self,timer):
        self.__target__ = timer

    def act(self,*args):
        args[3].remove(self.__target__)