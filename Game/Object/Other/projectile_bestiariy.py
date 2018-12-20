from Game.Action.Other.ProjectileDamageActions import Splash, Target
from Game.Object.Other.Projectile import MonsterTargetProjectile

bestiariy = { "arrow" : (MonsterTargetProjectile,{"speed" : 0.50, "name" : "arrow", "dmg" : 100, "dmg_type" : Target, "splash_range":0})}

def get_projectile_stats(name):
    return bestiariy[name]