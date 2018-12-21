import sys

from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from Game.Action.Tower.UpgradeTowerAction import UpgradeTowerAction
from Game.geometry import get_distance
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
game_object_drawer = GameObjectDrawer(game_session)
observer = ObservVidget()

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
                            observer.__target__ = tower
            if pygame.mouse.get_pressed()[0]:
                for tower in game_session.args[2]:
                    if get_distance(pygame.mouse.get_pos(), tower.get_cords()) <= 30:
                        game_session.args[3].add(UpgradeTowerAction(tower))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_session.args[3].add(ConstructTowerAction(pygame.mouse.get_pos(),"archery"))
            if event.key == pygame.K_w:
                game_session.args[3].add(ConstructTowerAction(pygame.mouse.get_pos(), "canon"))

    pygame.display.update()
    inject.instance(IWindowProvider)().get_window().fill((0,0,0))
    for action in game_object_drawer.get_actions():
        action.act(inject.instance(IWindowProvider)().get_window())
    window = inject.instance(IWindowProvider)().get_window()
    window.blit(observer.get_vidget(),(window.get_width() - 200,0))
print("DEFEAT")

pygame.quit()

