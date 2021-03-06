from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Other.EmptyAction import EmptyAction
from Game.Action.Other.RemoveTimerFromTracker import RemoveTimerFromTracker
from Game.Action.Other.TimerAction import TimerAction
from Game.Object.Infrastructer.ITimer import ITimer


class Timer(ITimer, IGameActionHolder):
    def __init__(self,time_in_milliseconds):
        self.time = time_in_milliseconds
        self.elipsed_time = self.time

    def get_time(self):
        return self.elipsed_time

    def rerun(self):
        self.elipsed_time = self.time

    def get_actions(self):
        if self.elipsed_time > 0:
            return [TimerAction(self)]#timer action
        else:
            return []

    def reset(self):
        self.elipsed_time = self.time
