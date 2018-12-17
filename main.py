from init import init
from Game.GameSession import GameSession
from Game.Object.Other.Timer import Timer


init()
game_session = GameSession()
game_session.run()
print(game_session.args[0])