from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Tower.SearchMonsterTargetAction import SearchMonsterTargetAction
from Game.Object.Tower.BaseTower import BaseTower


class TargetTower(BaseTower, IGameActionHolder):
    def __init__(self,cords,range):
        BaseTower.__init__(self,cords,range)
        self.target = None
    def get_actions(self):
        if self.target == None:
            return [SearchMonsterTargetAction(self)]
