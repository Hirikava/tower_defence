from Game.Object.Tower.TargetTower import TargetTower

bestiariy = {"archery" : (TargetTower,{"range": 300,"cooldown" : 1000, "name":"archery" , "projectile" : "arrow"})}

def get_tower_stats(name):
    return bestiariy[name]


