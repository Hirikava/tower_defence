from Game.Action.Infrastructer.IGameAction import IGameAction


class RegisterProjectileAction(IGameAction):
    def __init__(self,projectile):
        self.__target__ = projectile

    def act(self,*args):
        args[5].add(self.__target__)