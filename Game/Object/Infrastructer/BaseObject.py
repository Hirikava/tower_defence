from Game.Object.Infrastructer.IGameObject import IGameObject


class BaseObject(IGameObject):
    def __init__(self,cords):
        self.cords = cords

    def get_cords(self):
        return self.cords
