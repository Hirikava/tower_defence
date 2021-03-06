import inject
import pygame

from Graphics.Interfaces.IWindowProvider import IWindowProvider
from Graphics.Object.Drawers.GameObjectDrawer import GameObjectDrawer
from Graphics.Object.Drawers.UIObjectDrawer import UIObjectDrawer
from Graphics.View.CamerView import CameraView


class GraphicsSession():
    def __init__(self,game_session,ui_session):
        self.game_session = game_session
        self.game_object_drawer = GameObjectDrawer(game_session)
        self.ui_object_drawer = UIObjectDrawer(ui_session)


    def run(self):
        pygame.display.update()
        inject.instance(IWindowProvider)().get_window().fill((0, 0, 0))
        for action in self.game_object_drawer.get_actions():
            action.act(inject.instance(IWindowProvider)().get_window())

        for action in self.ui_object_drawer.get_actions():
            action.act(inject.instance(IWindowProvider)().get_window())
        # window = inject.instance(IWindowProvider)().get_window()
        # window.blit(self.observer.get_vidget(), (window.get_width() - 200, 0))
