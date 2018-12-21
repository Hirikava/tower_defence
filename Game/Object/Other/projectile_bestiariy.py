from Game.Action.Other.ProjectileDamageActions import Splash, Target
from Game.Object.Other.Projectile import MonsterTargetProjectile

bestiariy = { "arrow" : (MonsterTargetProjectile,{"speed" : 0.50, "name" : "arrow", "dmg" : 100, "dmg_type" : Target, "splash_range":0}),
              "arrow*" : (MonsterTargetProjectile,{"speed" : 0.55, "name" : "arrow", "dmg" : 130, "dmg_type" : Target, "splash_range":0}),
              "arrow**" : (MonsterTargetProjectile,{"speed" : 0.55, "name" : "arrow", "dmg" : 170, "dmg_type" : Target, "splash_range":0}),
              "yadro" : (MonsterTargetProjectile,{"speed" : 0.30, "name" : "yadro", "dmg" : 170, "dmg_type" : Splash, "splash_range":70}),
              "yadro*" : (MonsterTargetProjectile,{"speed" : 0.30, "name" : "yadro", "dmg" : 300, "dmg_type" : Splash, "splash_range":140}),
              "yadro**" : (MonsterTargetProjectile,{"speed" : 0.30, "name" : "yadro", "dmg" : 410, "dmg_type" : Splash, "splash_range":240}),
              }

def get_projectile_stats(name):
    return bestiariy[name]