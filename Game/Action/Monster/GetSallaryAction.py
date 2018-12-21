from Game.Action.Infrastructer.IGameAction import IGameAction


class GetSallaryAction(IGameAction):
    def __init__(self, monster):
        self.__target__ = monster

    def act(self,*args):
        args[4].gold += self.__target__.sallary