from Game.Action.Infrastructer.IGameActionHolder import IGameActionHolder
from Game.Action.Monster.SpawnMonsterAction import SpawnMonsterAction
from Game.Action.Other.EndTimeAction import EndTimeAction
from Game.GameLoader import GameLoader
from Game.Object.Other.Tracker import Tracker
from Game.Object.Tower.TargetTower import TargetTower
from Settings.GameSessionSetingsProvider import IGameSessionSettingsProvider
from Time.Clock import Clock
import inject


class GameSession(IGameActionHolder):
    def __init__(self,level):
        self.clock = Clock()
        game_scenario = GameLoader().load(level)
        self.gold = game_scenario["gold"]
        self.life = game_scenario["life_counter"]
        self.args = list([0,Tracker(),Tracker(),Tracker(),self])
        self.__track_monster_spawn__(game_scenario)
        settings = inject.instance(IGameSessionSettingsProvider)().get_settings()
        self.min_time_delay = int(settings['min_time_delay'])


    def run(self):
        self.clock.tick()
        for i in range(1,4):
            for action_holder in self.args[i]:
                for action in action_holder.get_actions():
                    action.act(*self.args)
        self.clock.delay(self.min_time_delay)
        self.clock.tick()
        self.args[0] = self.clock.get_time()

    def __track_monster_spawn__(self,game_scenario):
        for spawn in game_scenario["spawn_monsters"]:
            self.args[3].add(EndTimeAction(SpawnMonsterAction(spawn[1],game_scenario['spawner_pos'],game_scenario["track"]),int(spawn[0])))