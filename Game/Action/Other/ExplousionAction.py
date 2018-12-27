from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.Object.Tower.tower_bestiariy import get_tower_stats
from Game.geometry import get_distance


class ExplousionAction(IGameAction):
    def __init__(self,cords,name):
        self.cords = cords
        self.name = name

    def act(self,*args):
        stats = get_tower_stats(self.name)
        if stats["price"] <= args[4].gold:
            args[4].gold -= stats["price"]
            for monster in args[1]:
                if get_distance(self.cords,monster.get_cords()) < stats["range"]:
                    monster.current_hp -= stats["dmg"] * (1 - monster.armour/100)
        args[3].remove(self)