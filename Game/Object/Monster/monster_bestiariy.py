from Game.Object.Monster.BaseMonster import BaseMonster
from Game.Object.Monster.TrackedMonster import TrackedMonster

bestiariy = {
    "skeleton" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"skeleton","sallary" : 10, "armour":0}),
    "armored_skeleton" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"armored_skeleton","sallary" : 15, "armour":50}),
}

def get_monster_stats(name):
    return bestiariy[name]