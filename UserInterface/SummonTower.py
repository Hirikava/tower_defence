from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from UserInterface.IUIAction import IUIAction


class ButtonSummonTower(IUIAction):
    def __init__(self,tower_name):
        self.tower_name = tower_name

    def act(self,*args):
        args[1].next_click_action =  SummmonTower(self.tower_name)





class SummmonTower(IUIAction):
    def __init__(self,name):
        self.name = name

    def act(self,*args):
        args[2].args[3].add(ConstructTowerAction(args[1].mous_pos,self.name))
