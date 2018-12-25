import sys
from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from Game.Action.Tower.UpgradeTowerAction import UpgradeTowerAction
from Game.geometry import get_distance
from Graphics.GraphicsSession import GraphicsSession
from Graphics.Interfaces.IWindowProvider import IWindowProvider
from Graphics.Object.Drawers.GameObjectDrawer import GameObjectDrawer
from UserInterface.ObservVidget import ObservVidget
from init import init
from Game.GameSession import GameSession
import pygame
import inject

pygame.init()
init()


inject.instance(IWindowProvider)().get_window()
game_session = GameSession(sys.argv[1])
graphics_session = GraphicsSession(game_session)
game_object_drawer = GameObjectDrawer(game_session)


while game_session.args[4].life > 0:
    game_session.run()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                for i in range(1,3):
                    for tower in game_session.args[i]:
                        if get_distance(pygame.mouse.get_pos(),tower.get_cords()) <= 30:
                            graphics_session.observer.__target__ = tower
            if pygame.mouse.get_pressed()[0]:
                for tower in game_session.args[2]:
                    if get_distance(pygame.mouse.get_pos(), tower.get_cords()) <= 30:
                        game_session.args[3].add(UpgradeTowerAction(tower))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_session.args[3].add(ConstructTowerAction(pygame.mouse.get_pos(),"archery"))
            if event.key == pygame.K_w:
                game_session.args[3].add(ConstructTowerAction(pygame.mouse.get_pos(), "canon"))

    graphics_session.run()


print("DEFEAT")

pygame.quit()

