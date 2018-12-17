from Game.Action.Infrastructer.IGameAction import IGameAction


class TimerAction(IGameAction):
    def __init__(self,timer):
        self.__target__ = timer

    def act(self,*args):
        self.__target__.elipsed_time -= args[0]
        if self.__target__.elipsed_time < 0:
            self.__target__.elipsed_time == 0