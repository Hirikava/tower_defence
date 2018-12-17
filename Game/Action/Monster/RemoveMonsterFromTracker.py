from Game.Action.Infrastructer.IGameAction import IGameAction


class RemoveMonsterFromTracker(IGameAction):
    def __init__(self, monster):
        self.__target__ = monster

    def act(self,*args):
        args[1].remove(self.__target__)