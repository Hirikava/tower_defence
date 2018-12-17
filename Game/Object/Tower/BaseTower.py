from Game.Object.Infrastructer.BaseObject import BaseObject
from Game.Object.Infrastructer.IGameObject import IGameObject
import abc

class ITower():
    @abc.abstractmethod
    def get_range(self):
        raise NotImplementedError


class BaseTower(BaseObject,ITower):
    def __init__(self,cords,range):
        BaseObject.__init__(self,cords)
        self.range = range

    def get_range(self):
        return self.range


