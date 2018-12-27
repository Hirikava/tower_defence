from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.geometry import get_distance


class SearchMonsterTargetAction(IGameAction):
    def __init__(self,target_tower):
        self.__target__ = target_tower

    def act(self,*args):
        for monster in args[1]:
            correct_type = True
            for type in monster.type:
                if type in self.__target__.banned_types:
                    correct_type = False

            if get_distance(self.__target__.get_cords(),monster.get_cords()) <= self.__target__.get_range() and correct_type:
                self.__target__.target = monster
                return
