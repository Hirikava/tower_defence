from Game.Object.Tower.TargetTower import TargetTower

bestiariy = {"archery" : (TargetTower,{"range": 300,"cooldown" : 1000, "name":"archery" , "projectile" : "arrow", "price":100, "upgrade_price":100,"banned_types":{}}),
             "archery*" : (TargetTower,{"range": 350,"cooldown" : 850, "name":"archery*" , "projectile" : "arrow*", "upgrade_price" : 200,"banned_types":{}}),
             "archery**" : (TargetTower,{"range": 400,"cooldown" : 600, "name":"archery**" , "projectile" : "arrow**", "upgrade_price" : "MaxLvl","banned_types":{}}),
             "canon" : (TargetTower,{"range": 200,"cooldown" : 2000, "name":"canon" , "projectile" : "yadro", "upgrade_price" : 200 , "price" : 100,"banned_types":{"flying",}}),
             "canon*" : (TargetTower,{"range": 200,"cooldown" : 1500, "name":"canon*" , "projectile" : "yadro*", "upgrade_price" : 400,"banned_types":{"flying",}}),
             "canon**" : (TargetTower,{"range": 200,"cooldown" : 1000, "name":"canon**" , "projectile" : "yadro**", "upgrade_price" : "MaxLvl","banned_types":{"flying",}}),
             "explousion" : {"price":100,"dmg":200,"range":400}}

def get_tower_stats(name):
    return bestiariy[name]


