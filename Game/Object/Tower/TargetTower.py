from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Other.TimerAction import TimerAction
from Game.Action.Tower.SearchMonsterTargetAction import SearchMonsterTargetAction
from Game.Object.Other.Timer import Timer
from Game.Object.Tower.BaseTower import BaseTower


class TargetTower(BaseTower, IGameActionHolder):
    def __init__(self,cords,range,cooldown):
        BaseTower.__init__(self,cords,range)
        self.target = None
        self.cooldown_timer = Timer(cooldown)

    def get_actions(self):
        if self.target == None:
            return [SearchMonsterTargetAction(self),TimerAction(timer=self.cooldown_timer)]
        elif self.cooldown_timer.elipsed_time == 0:
            self.cooldown_timer = self.cooldown_timer.time
            return [] #AtackAction
        else:
            return [TimerAction(self.cooldown_timer)] #TimerAction

