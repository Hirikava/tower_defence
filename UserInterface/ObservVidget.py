import pygame
import Game.Object.Monster.monster_bestiariy as mb
import Game.Object.Tower.tower_bestiariy as tb
from Graphics.Object.drawing_bestiariy import get_drawing_instance


class ObservVidget():
    def __init__(self):
        self.__target__ = None
        self.surface = pygame.Surface((200,200))
        self.surface.set_colorkey(self.surface.get_at((0,0)))
        self.surface = self.surface.convert_alpha()

    def get_surface(self):
        return self.surface

    def update_vidget(self):
        self.surface.fill((128,128,128))
        if self.__target__ != None:
            self.surface.blit(get_drawing_instance(self.__target__.name),(0,0))
            offset = 40
            if(mb.bestiariy.__contains__(self.__target__.name)):
                for key in mb.bestiariy[self.__target__.name][1]:
                    offset += 10
                    myfont = pygame.font.SysFont('Comic Sans MS', 10)
                    self.surface.blit(myfont.render('{0}: {1}'.format(key,mb.bestiariy[self.__target__.name][1][key]), False, (255, 242, 0)),(0,offset))
            elif (tb.bestiariy.__contains__(self.__target__.name)):
                for key in tb.bestiariy[self.__target__.name][1]:
                    offset += 10
                    myfont = pygame.font.SysFont('Comic Sans MS', 10)
                    self.surface.blit(
                        myfont.render('{0}: {1}'.format(key, tb.bestiariy[self.__target__.name][1][key]), False,
                                      (255, 242, 0)), (0, offset))