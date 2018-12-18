from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.geometry import get_distance


class UpdateTargetAction(IGameAction):
    def __init__(self,tower):
        self.__target__ = tower

    def act(self,*args):
        if not args[1].contains(self.__target__.target):
            self.__target__.target = None
        elif get_distance(self.__target__.get_cords(),self.__target__.target.get_cords()) > self.__target__.get_range():
            self.__target__.target = None
