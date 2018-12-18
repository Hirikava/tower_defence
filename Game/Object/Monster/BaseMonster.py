from Game import geometry
from Game.Object.Infrastructer.BaseObject import BaseObject


class BaseMonster(BaseObject):
    def __init__(self,cords,**kwargs):
        BaseObject.__init__(self,cords)
        self.speed = kwargs["speed"]
        self.hp = kwargs["hp"]

    def move_to(self,pos,time_span):
        vector = geometry.normalize_vector(geometry.get_direction_vector(self.cords,pos))
        distance = geometry.get_distance(self.cords,pos)
        if distance <= self.speed * time_span:
            self.cords = pos
            return True
        self.cords = (self.cords[0] + vector[0] * self.speed * time_span,
                        self.cords[1] + vector[1] * self.speed * time_span)






