from Game.Action.Tower.ConstructTowerAction import ConstructTowerAction
from Graphics.View.CamerView import CameraView
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
        camera = CameraView().get_view_point()
        args[2].args[3].add(ConstructTowerAction((args[1].mous_pos[0] + camera[0],args[1].mous_pos[1] + camera[1]),self.name))
