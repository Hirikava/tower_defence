from Game.Object.Tower.TargetTower import TargetTower

bestiariy = {"archery" : (TargetTower,{"range": 300,"cooldown" : 1000, "name":"archery" , "projectile" : "arrow", "price":100, "upgrade_price":100}),
             "archery*" : (TargetTower,{"range": 350,"cooldown" : 850, "name":"archery*" , "projectile" : "arrow*", "upgrade_price" : 200}),
             "archery**" : (TargetTower,{"range": 400,"cooldown" : 600, "name":"archery**" , "projectile" : "arrow**", "upgrade_price" : "MaxLvl"}),
             "canon" : (TargetTower,{"range": 200,"cooldown" : 2000, "name":"canon" , "projectile" : "yadro", "upgrade_price" : 200 , "price" : 100}),
             "canon*" : (TargetTower,{"range": 200,"cooldown" : 1500, "name":"canon*" , "projectile" : "yadro*", "upgrade_price" : 400}),
             "canon**" : (TargetTower,{"range": 200,"cooldown" : 1000, "name":"canon**" , "projectile" : "yadro**", "upgrade_price" : "MaxLvl"}),
             "explousion" : {"price":100,"dmg":200,"range":400}}

def get_tower_stats(name):
    return bestiariy[name]


