from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.geometry import get_distance


class SearchMonsterTargetAction(IGameAction):
    def __init__(self,target_tower):
        self.__target__ = target_tower

    def act(self,*args):
        for monster in args[1]:
            if get_distance(self.__target__.get_cords(),monster.get_cords) <= self.__target__.get_range():
                self.__target__ = monster
