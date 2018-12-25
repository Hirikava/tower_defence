from singleton_decorator import singleton
import inject

from Graphics.Interfaces.IWindowProvider import IWindowProvider


@singleton
class CameraView():
    def __init__(self):
        window_provider = inject.instance(IWindowProvider)
        self.view_size = window_provider().get_window().get_size()
        self.view_point = (0,0)

    def move_camera(self,vector):
        self.view_point = (self.view_point[0] + vector[0],vector[1] + self.view_point[1])

    def get_view_point(self):
        return self.view_point