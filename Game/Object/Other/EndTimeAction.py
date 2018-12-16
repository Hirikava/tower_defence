from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Other.RemoveTimerFromTracker import RemoveTimerFromTracker
from Game.Action.Other.TimerAction import TimerAction
from Game.Object.Other.Timer import Timer

class EndTimeAction(Timer):
    def __init__(self,inner_action_holer,time_in_milliseconds):
        Timer.__init__(self,time_in_milliseconds=time_in_milliseconds)
        self.__inner_action_holder__ = inner_action_holer

    @property
    def get_actions(self):
        if self.get_time() > 0:
            return [TimerAction(self)]
        else:
            ret_actions = self.__inner_action_holder__.get_actions()
            ret_actions.append(RemoveTimerFromTracker(self))
            return ret_actions
