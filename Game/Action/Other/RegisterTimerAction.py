from Game.Action.Infrastructer.IGameAction import IGameAction


class RegisterTimerAction(IGameAction):
    def __init__(self,timer):
        self.__target__ = timer

    def act(self,*args):
        args[3].add(self.__target__)