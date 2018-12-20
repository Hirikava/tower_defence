from Game.Action.Infrastructer.IGameAction import IGameAction


class ProjectileToMonsterMoveAction(IGameAction):
    def __init__(self,projectile):
        self.__target__ = projectile

    def act(self,*args):
        self.__target__.on_target = self.__target__.move_to(self.__target__.target_monster.get_cords(),args[0])
