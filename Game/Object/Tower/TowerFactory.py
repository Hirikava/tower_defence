from Game.Object.Tower.tower_bestiariy import get_tower_stats


class TowerFactory():
    def get_instance(self,name,cords):
        stats = get_tower_stats(name)
        return stats[0](cords,**stats[1])
