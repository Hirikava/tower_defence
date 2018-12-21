from Graphics.Object.Infrastructure.IGraphicsAction import IGraphicsAction
from Graphics.Object.drawing_bestiariy import get_drawing_instance

import pygame

class CreatureDrawAction(IGraphicsAction):
    def __init__(self,creature):
        self.__target__ = creature

    def act(self,*args):
        window = args[0]
        drawing_surface = get_drawing_instance(self.__target__.name)
        game_object_cords = self.__target__.get_cords()
        offset = (drawing_surface.get_width()/2,drawing_surface.get_height()/2)
        drawing_object_cords = (game_object_cords[0] - offset[0] ,game_object_cords[1] - offset[1])
        window.blit(drawing_surface,drawing_object_cords)
        DrawHpBarAction(self.__target__).act(offset,*args)

class DrawHpBarAction(IGraphicsAction):#GraphicsActon
    def __init__(self,creature):
        self.__target__ = creature

    def act(self,offset,*args):
        pos = self.__target__.get_cords()
        pygame.draw.rect(args[0], (255,0,0), (pos[0] - offset[0], pos[1] - offset[1] - 10, 20, 10))
        hp_persentage = self.__target__.current_hp / self.__target__.hp
        if hp_persentage < 0:
            hp_persentage = 0
        pygame.draw.rect(args[0], (0,255,0), (pos[0] - offset[0], pos[1] - offset[1] - 10, 20 * hp_persentage,10))


class TowerDrawAction(IGraphicsAction):
    def __init__(self,tower):
        self.__target__ = tower

    def act(self,*args):
        window = args[0]
        drawing_surface = get_drawing_instance(self.__target__.name)
        game_object_cords = self.__target__.get_cords()
        drawing_object_cords = (game_object_cords[0] - drawing_surface.get_width()/2,game_object_cords[1] - drawing_surface.get_height()/2)
        window.blit(drawing_surface,drawing_object_cords)
        DrawRangeAction(self.__target__).act(*args)

class DrawRangeAction(IGraphicsAction):
    def __init__(self,tower):
        self.__target__ = tower
    def act(self,*args):
        pygame.draw.circle(args[0], (255, 0, 0), self.__target__.get_cords(),self.__target__.get_range(), 1)


class ProjectileDrawAction(IGraphicsAction):
    def __init__(self,projectile):
        self.__target__ = projectile
    def act(self,*args):
        window = args[0]
        drawing_surface = get_drawing_instance(self.__target__.name)
        game_object_cords = self.__target__.get_cords()
        drawing_object_cords = (
        game_object_cords[0] - drawing_surface.get_width() / 2, game_object_cords[1] - drawing_surface.get_height() / 2)
        window.blit(drawing_surface, drawing_object_cords)

class DrawGoldAmount(IGraphicsAction):
    def __init__(self,gold):
        self.__gold__ = gold

    def act(self,*args):
        window = args[0]
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        window.blit(myfont.render('gold: {0}'.format(self.__gold__),False,(255,242,0)),(0,0))

class DrawLifeAmount(IGraphicsAction):
    def __init__(self,life):
        self.__life__ = life

    def act(self,*args):
        window = args[0]
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        surface = myfont.render('life: {0}'.format(self.__life__),False,(0,255,0))
        window.blit(surface,(0,window.get_height() - surface.get_height()))


