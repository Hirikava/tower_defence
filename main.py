from Game.Object.Other.Timer import Timer

timer = Timer(500)
actor = timer.get_actions()[0]
actor.act(50)
print(timer.get_time())