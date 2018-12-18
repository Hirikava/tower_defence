import pygame
from Graphics.Interfaces.ILoadTextureInterface import ILoadTextureInterface

def load_texture_config(binder):
    binder.bind(ILoadTextureInterface,PygameLoadInterface)

class PygameLoadInterface(ILoadTextureInterface):
    def load(self,filename):
        texture = pygame.image.load(filename)
        texture.set_colorkey(texture.get_at((0,0)))
        return texture.convert_alpha()
