from Game.Action.Infrastructer.IGameAction import IGameAction


class TimerAction(IGameAction):
    def __init__(self,timer):
        self.__taget__ = timer

    def act(self,*args):
        self.__taget__.time -= args[0]