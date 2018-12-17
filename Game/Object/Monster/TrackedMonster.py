from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Monster.MoveAction import MoveAction
from Game.Action.Monster.ReduceLifeCounter import ReduceLifeCounter
from Game.Action.Monster.RemoveMonsterFromTracker import RemoveMonsterFromTracker
from Game.Object.Monster.BaseMonster import BaseMonster

class TrackedMonster(BaseMonster, IGameActionHolder):
    def __init__(self,cords,speed,track,hp):
        BaseMonster.__init__(self,cords,hp,speed)
        self.track = track
        self.track_counter = 0

    def get_actions(self):
        if self.hp <= 0:
            return [RemoveMonsterFromTracker(self)]
        elif self.track_counter == len(self.track):
            return [RemoveMonsterFromTracker(self),ReduceLifeCounter()]
        else:
            return [MoveAction(self)]

