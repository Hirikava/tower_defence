from init import init
from Game.GameSession import GameSession
import pygame


init()
pygame.init()
window = pygame.display.set_mode((1200,900))
monster_text = pygame.image.load("Assets\\monster.png")
tower_text = pygame.image.load("Assets\\tower.png")
game_session = GameSession("level1.td")

while game_session.args[4].life > 0:
    game_session.run()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    window.fill((0,0,0))
    for tower in game_session.args[2]:
        window.blit(tower_text,tower.get_cords())
        pygame.draw.circle(window,(255,0,0),tower.get_cords(),tower.get_range(),1)
    for monster in game_session.args[1]:
        window.blit(monster_text,monster.get_cords())

pygame.quit()

