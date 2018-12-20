from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Monster.RemoveMonsterFromTracker import RemoveMonsterFromTracker
from Game.Action.Other.ProjectileToMonsterMoveAction import ProjectileToMonsterMoveAction
from Game.Action.Other.RemoveProjectileFromTracker import RemoveProjectileFromTracker
from Game.Object.Infrastructer.BaseObject import BaseObject
from Game import geometry


class BaseProjectile(IGameActionHolder,BaseObject):
    def __init__(self,cords,**stats):
        BaseObject.__init__(self,cords,**stats)
        self.dmg = stats["dmg"]
        self.speed = stats["speed"]
        self.dmg_action = stats["dmg_type"]
        self.splash_range = stats["splash_range"]


class MonsterTargetProjectile(BaseProjectile):
    def __init__(self,cords,target,**stats):
        BaseProjectile.__init__(self,cords,**stats)
        self.target_monster = target
        self.on_target = False

    def move_to(self, pos, time_span):
        vector = geometry.normalize_vector(geometry.get_direction_vector(self.cords,pos))
        distance = geometry.get_distance(self.cords,pos)
        if distance <= self.speed * time_span:
            self.cords = pos
            return True
        self.cords = (self.cords[0] + vector[0] * self.speed * time_span,
                        self.cords[1] + vector[1] * self.speed * time_span)

    def get_actions(self):
        if self.on_target:
            return [RemoveProjectileFromTracker(self),self.dmg_action(self)]
        return [ProjectileToMonsterMoveAction(self)]
