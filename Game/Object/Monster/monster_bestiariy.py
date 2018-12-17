from Game.Object.Monster.BaseMonster import BaseMonster
from Game.Object.Monster.TrackedMonster import TrackedMonster

bestiariy = { "monster" : (TrackedMonster,{"hp":100,"speed" : 0.25})}

def get_monster_stats(name):
    return bestiariy[name]