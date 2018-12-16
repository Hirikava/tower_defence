from Game.Action.Infrastructer.IGameAction import IGameAction


class EmptyAction(IGameAction):
    def __int__(self,*args):
        pass

    def act(self,*args):
        pass