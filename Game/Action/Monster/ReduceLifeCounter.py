from Game.Action.Infrastructer.IGameAction import IGameAction

class ReduceLifeCounter(IGameAction):
    def act(self,*args):
        args[4] -= 1