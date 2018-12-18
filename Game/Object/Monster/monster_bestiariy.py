from Game.Object.Monster.BaseMonster import BaseMonster
from Game.Object.Monster.TrackedMonster import TrackedMonster

bestiariy = { "monster" : (TrackedMonster,{"hp":300,"speed" : 0.15})}

def get_monster_stats(name):
    return bestiariy[name]