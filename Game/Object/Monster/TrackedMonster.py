from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Monster.GetSallaryAction import GetSallaryAction
from Game.Action.Monster.MoveAction import MoveAction
from Game.Action.Monster.ReduceLifeCounter import ReduceLifeCounter
from Game.Action.Monster.RemoveMonsterFromTracker import RemoveMonsterFromTracker
from Game.Object.Monster.BaseMonster import BaseMonster

class TrackedMonster(BaseMonster, IGameActionHolder):
    def __init__(self,cords,track,**stats):
        BaseMonster.__init__(self,cords,**stats)
        self.current_hp = self.hp
        self.track = track
        self.track_counter = 0

    def get_actions(self):
        if self.current_hp <= 0:
            return [RemoveMonsterFromTracker(self),GetSallaryAction(self)]
        elif self.track_counter == len(self.track):
            return [RemoveMonsterFromTracker(self),ReduceLifeCounter()]
        else:
            return [MoveAction(self)]

