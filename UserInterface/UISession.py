import inject
import pygame

from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from Game.Action.Tower.UpgradeTowerAction import UpgradeTowerAction
from Game.Object.Other.Tracker import Tracker
from Game.geometry import get_distance
from Graphics.Interfaces.IWindowProvider import IWindowProvider
from Graphics.Object.drawing_bestiariy import get_drawing_instance
from Settings.SettingsReader import SettingsReader
from UserInterface.Button import Button
from UserInterface.ObservVidget import ObservVidget
from UserInterface.SummonTower import ButtonSummonTower


class UISession():
    def __init__(self,game_session, UITowerIni):
        self.mous_pos = (0,0)
        self.game_session = game_session
        self.next_click_action = None
        self.args = [Tracker(),self,self.game_session]
        self.was_action = False
        self.observer = ObservVidget()

        towers = SettingsReader().read(UITowerIni)["tower_set"].split(",")
        window = inject.instance(IWindowProvider)().get_window()
        offset = 0
        for tower in towers:
            tower = tower.replace("\n","")
            surface = get_drawing_instance(tower)
            self.args[0].add(Button(ButtonSummonTower(tower),(offset,window.get_height() - surface.get_height()),(surface.get_width(),surface.get_height()),tower))
            offset += surface.get_width()


    def run(self):
        self.mous_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for button in self.args[0]:
                        if button.on_click(self.mous_pos):
                            button.get_actions().act(*self.args)
                            self.was_action = True
                if self.was_action == False:
                    if self.next_click_action != None:
                        self.next_click_action.act(*self.args)
                        self.next_click_action = None

                if pygame.mouse.get_pressed()[2]:
                     for i in range(1, 3):
                         for tower in self.game_session.args[i]:
                             if get_distance(pygame.mouse.get_pos(), tower.get_cords()) <= 30:
                                 self.observer.__target__ = tower
                if pygame.mouse.get_pressed()[0]:
                    for tower in self.game_session.args[2]:
                         if get_distance(pygame.mouse.get_pos(), tower.get_cords()) <= 30:
                             self.game_session.args[3].add(UpgradeTowerAction(tower))


        self.was_action = False

    def get_button_set(self):
        return self.args[0]