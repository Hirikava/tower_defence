from singleton_decorator import singleton
import inject

from Graphics.Interfaces.IWindowProvider import IWindowProvider


@singleton
class CameraView():
    def __init__(self):
        window_provider = inject.instance(IWindowProvider)
        self.view_size = window_provider().get_window().get_size()
        self.max_view = None
        self.view_point = (0,0)

    def move_camera(self,vector):
        self.view_point = (self.view_point[0] + vector[0],vector[1] + self.view_point[1])
        if self.view_point[0] < 0:
            self.view_point = (0,self.view_point[1])
        if self.view_point[1] < 0:
            self.view_point = (self.view_point[0], 0)

        if self.max_view != None:
            if self.view_point[0] > self.max_view[0]:
                self.view_point = (self.max_view[0],self.view_point[1])
            if self.view_point[1] > self.max_view[1]:
                self.view_point = (self.view_point[0], self.max_view[1])
    def get_view_point(self):
        return self.view_point