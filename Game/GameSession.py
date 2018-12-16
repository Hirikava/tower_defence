from Game.Object.Other.Tracker import Tracker
from Time.Clock import Clock


class GameSession():
    def __init__(self):
        self.clock = Clock()
        self.args = [0,Tracker(),Tracker(),Tracker()]

    def run(self):
        pass #TO DO