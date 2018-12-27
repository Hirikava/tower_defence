from Game.Object.Monster.Bosses import SkeletonKing
from Game.Object.Monster.TrackedMonster import TrackedMonster

bestiariy = {
    "skeleton" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"skeleton","sallary" : 10, "armour":0, "type":list()}),
    "armored_skeleton" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"armored_skeleton","sallary" : 15, "armour":50, "type":list()}),
    "skeleton_king" : (SkeletonKing,{"hp":230,"speed" : 0.05, "name":"skeleton_king","sallary" : 15, "armour":50, "type":list()}),
    "bird" : (TrackedMonster,{"hp":230,"speed" : 0.05, "name":"bird","sallary" : 15, "armour":50, "type":{"flying"}}),
}

def get_monster_stats(name):
    return bestiariy[name]