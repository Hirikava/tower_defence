from Graphics.WindowProvider import WindowProvider
import pygame

class DrawHpBar():#GraphicsActon
    def __init__(self,tracked_monster):
        self.__target__ = tracked_monster

    def act(self):
        pos = self.__target__.get_cords()
        pygame.draw.rect(WindowProvider().get_window(),(255,0,0),(pos[0],pos[1] - 10,20,10))
        hp_persentage = self.__target__.current_hp / self.__target__.hp
        pygame.draw.rect(WindowProvider().get_window(),(0,255,0),(pos[0],pos[1] - 10,20 * hp_persentage,10))
