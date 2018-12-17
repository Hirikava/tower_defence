from Time.IClock import IClock
import pygame

class Clock(IClock):
    def __init__(self):
        self.__clock__ = pygame.time.Clock()

    def tick(self):
        self.__clock__.tick()

    def get_time(self):
        return self.__clock__.get_time()

    def delay(self,time_span):
        pygame.time.delay(time_span)