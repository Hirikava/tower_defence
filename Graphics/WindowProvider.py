from Graphics.IWindowProvider import IWindowProvider
from singleton_decorator import singleton
import pygame

from Settings.SettingsReader import SettingsReader

@singleton
class WindowProvider(IWindowProvider):
    def __init__(self):
        settings = SettingsReader().read('graphics.ini')
        res_token = settings["resolution"].split(",")
        self.__window__ = pygame.display.set_mode((int(res_token[0]),int(res_token[1])))
        pygame.display.set_caption(settings["title"])

    def get_window(self):
        return self.__window__