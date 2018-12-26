import sys
from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from Game.Action.Tower.UpgradeTowerAction import UpgradeTowerAction
from Game.geometry import get_distance
from Graphics.GraphicsSession import GraphicsSession
from Graphics.Interfaces.IWindowProvider import IWindowProvider
from Graphics.Object.Drawers.GameObjectDrawer import GameObjectDrawer
from UserInterface.ObservVidget import ObservVidget
from UserInterface.UISession import UISession
from init import init
from Game.GameSession import GameSession
import pygame
import inject

pygame.init()
init()


inject.instance(IWindowProvider)().get_window()
game_session = GameSession(sys.argv[1])
uisession = UISession(game_session,"ui.ini")
graphics_session = GraphicsSession(game_session,uisession)
game_object_drawer = GameObjectDrawer(game_session)



while game_session.args[4].life > 0:
    uisession.run()
    game_session.run()
    graphics_session.run()

print("DEFEAT")

pygame.quit()

