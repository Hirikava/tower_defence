from Game.Object.Infrastructer.IGameObject import IGameObject


class BaseObject(IGameObject):
    def __init__(self,cords,**stats):
        self.cords = cords
        self.name = stats['name']

    def get_cords(self):
        return self.cords
