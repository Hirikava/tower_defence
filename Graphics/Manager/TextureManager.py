from singleton_decorator import singleton
import inject
import pygame

from Graphics.Interfaces.ILoadTextureInterface import ILoadTextureInterface


@singleton
class TextureManager():
    def __init__(self):
        self.__buffer__ = dict()

    def load_texture(self,filename):
        buf_key = hash(filename)
        if buf_key in self.__buffer__:
            return self.__buffer__[buf_key]
        else:
            self.__buffer__[buf_key] = inject.instance(ILoadTextureInterface)().load(filename)
        return self.__buffer__[buf_key]

    def clear(self):
        self.__buffer__.clear()