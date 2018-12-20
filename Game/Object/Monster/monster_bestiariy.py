from Game.Object.Monster.BaseMonster import BaseMonster
from Game.Object.Monster.TrackedMonster import TrackedMonster

bestiariy = { "skeleton" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"skeleton"})}

def get_monster_stats(name):
    return bestiariy[name]