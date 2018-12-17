from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Object.Other.Tracker import Tracker
from Settings.GameSessionSetingsProvider import IGameSessionSettingsProvider
from Time.Clock import Clock
import inject


class GameSession(IGameActionHolder):
    def __init__(self):
        self.clock = Clock()
        self.life_counter = 10
        self.args = [0,Tracker(),Tracker(),Tracker(),self.life_counter]
        settings = inject.instance(IGameSessionSettingsProvider)().get_settings()
        self.min_time_delay = int(settings['min_time_delay'])

    def run(self):
        self.clock.tick()
        for i in range(1,4):
            for action_holder in self.args[i]:
                for action in action_holder.get_actions():
                    action.act(self.args)
        self.clock.delay(self.min_time_delay)
        self.clock.tick()
        self.args[0] = self.clock.get_time()
