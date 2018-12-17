from Game.Action.Infrastructer.IGameAction import IGameAction
from Game.Action.Monster.monster_bestiariy import get_monster_stats


class SpawnMonsterAction(IGameAction):
    def __init__(self,monster_name,cords,track):
        self.cords = cords
        self.name = monster_name
        self.track = track

    def act(self,*args):
        monster_stats = get_monster_stats(self.name)
        cls = monster_stats[0]
        stats = monster_stats[1]
        args[1].add(cls(cords=self.cords,track=self.track,**stats))

