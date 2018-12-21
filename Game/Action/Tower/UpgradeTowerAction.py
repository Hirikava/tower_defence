from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.Object.Tower.tower_bestiariy import bestiariy, get_tower_stats


class UpgradeTowerAction(IGameAction):
    def __init__(self,tower):
        self.__target__ = tower

    def act(self,*args):
        if bestiariy.__contains__(self.__target__.name + "*"):
            if args[4].gold >= get_tower_stats(self.__target__.name)[1]["upgrade_price"]:
                args[4].gold -= get_tower_stats(self.__target__.name)[1]["upgrade_price"]
                stats = get_tower_stats(self.__target__.name + "*")
                args[2].add(stats[0](self.__target__.get_cords(),**stats[1]))
                args[2].remove(self.__target__)
        args[3].remove(self)