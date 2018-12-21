from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.geometry import get_distance

class Splash(IGameAction):
    def __init__(self,projectile):
        self.__target__ = projectile

    def act(self,*args):
        for monster in args[1]:
            if get_distance(monster.get_cords(),self.__target__.get_cords()) < self.__target__.splash_range:
                monster.current_hp -= self.__target__.dmg

class Target(IGameAction):
    def __init__(self,projectile):
        self.__target__ = projectile

    def act(self,*args):
        self.__target__.target_monster.current_hp -= self.__target__.dmg * (1 - self.__target__.target_monster.armour/100)