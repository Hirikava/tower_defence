from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Other.TimerAction import TimerAction
from Game.Action.Tower.SearchMonsterTargetAction import SearchMonsterTargetAction
from Game.Action.Tower.UpdateTargetAction import UpdateTargetAction
from Game.Object.Other.Timer import Timer
from Game.Object.Tower.BaseTower import BaseTower


class TargetTower(BaseTower, IGameActionHolder):
    def __init__(self,cords,range,cooldown):
        BaseTower.__init__(self,cords,range)
        self.target = None
        self.cooldown_timer = Timer(cooldown)

    def get_actions(self):
        ret_actions = list()
        ret_actions.append(UpdateTargetAction(self))
        if self.target == None:
            ret_actions.append(SearchMonsterTargetAction(self))
        if self.cooldown_timer.elipsed_time != 0:
            ret_actions.append(TimerAction(self.cooldown_timer))

        if self.cooldown_timer.get_time() == 0 and self.target != None:
            self.cooldown_timer.reset()
            ret_actions.append(SimpleAttackAction(self.target,120)) #AtackAction
        return ret_actions

class SimpleAttackAction(IGameAction):
    def __init__(self,base_monster,dmg):
        self.__target__ = base_monster
        self.dmg = dmg
    def act(self,*args):
        self.__target__.current_hp -= self.dmg