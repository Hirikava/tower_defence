from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Monster.MoveAction import MoveAction
from Game.Object.Monster.BaseMonster import BaseMonster

class TrackedMonster(BaseMonster, IGameActionHolder):
    def __init__(self,cords,speed,track):
        BaseMonster.__init__(self,cords,speed)
        self.track = track
        self.track_counter = 0


    def get_actions(self):
        if self.track_counter == len(self.track):
            pass #Game Action if Monster Will Ends Track
        else:
            return [MoveAction(self)]

