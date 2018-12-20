from Graphics.DrawHpBar import DrawHpBar
from Graphics.Interfaces.IWindowProvider import IWindowProvider
from Graphics.Manager.TextureManager import TextureManager
from Graphics.Object.Drawers.GameObjectDrawer import GameObjectDrawer
from init import init
from Game.GameSession import GameSession
import pygame
import inject


init()
pygame.init()
window = pygame.display.set_mode((1200,900))

game_session = GameSession("level1.td")
game_object_drawer = GameObjectDrawer(game_session)
while game_session.args[4].life > 0:
    game_session.run()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    pygame.display.update()
    window.fill((0,0,0))
    for action in game_object_drawer.get_actions():
        action.act(inject.instance(IWindowProvider)().get_window())
    # for tower in game_session.args[2]:
    #     inject.instance(IWindowProvider)().get_window().blit(tower_text,tower.get_cords())
    #     pygame.draw.circle( inject.instance(IWindowProvider)().get_window(),(255,0,0),tower.get_cords(),tower.get_range(),1)
    # for monster in game_session.args[1]:
    #     inject.instance(IWindowProvider)().get_window().blit(monster_text,monster.get_cords())
    #     DrawHpBar(monster).act()
print("DEFEAT")

pygame.quit()

