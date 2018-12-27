from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.geometry import get_distance


class DestroyNearTowerAction(IGameAction):
    def __init__(self,monster):
        self.__target__ = monster

    def act(self,*args):
        towerTarget = None
        range = 10000000
        for tower in args[2]:
            if get_distance(self.__target__.get_cords(),tower.get_cords()) < range:
                range = get_distance(self.__target__.get_cords(),tower.get_cords())
                towerTarget = tower
        if towerTarget != None:
            args[2].remove(towerTarget)