from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.Object.Tower.tower_bestiariy import get_tower_stats
from Game.geometry import get_distance


class ConstructTowerAction(IGameAction):
    def __init__(self,cords,name):
        self.cords = cords
        self.name = name

    def act(self,*args):
        stats = get_tower_stats(self.name)
        valid = True
        for tower in args[2]:
            if get_distance(self.cords,tower.get_cords()) < 60:
                valid = False
        if valid and stats[1]["price"] <= args[4].gold:
            args[2].add(stats[0](self.cords,**stats[1]))
            args[4].gold -= stats[1]["price"]
        args[3].remove(self)