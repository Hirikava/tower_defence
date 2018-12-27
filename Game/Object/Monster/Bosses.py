from Game.Action.Monster.DestroyNearTowerAction import DestroyNearTowerAction
from Game.Object.Monster.BaseMonster import BaseMonster
from Game.Object.Monster.TrackedMonster import TrackedMonster


class SkeletonKing(TrackedMonster):
    def __init__(self, cords,track, **kwargs):
        TrackedMonster.__init__(self, cords,track, **kwargs)

    def get_actions(self):
        actions = TrackedMonster.get_actions(self)
        if self.current_hp <= 0:
            actions.append(DestroyNearTowerAction(self))
        return actions