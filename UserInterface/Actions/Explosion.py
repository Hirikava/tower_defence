from Game.Action.Other.ExplousionAction import ExplousionAction
from UserInterface.IUIAction import IUIAction


class ButtonExplousion(IUIAction):
    def __init__(self):
        pass

    def act(self,*args):
        args[1].next_click_action = Explousion()


class Explousion(IUIAction):
    def act(self,*args):
        args[2].args[3].add(ExplousionAction(args[1].mous_pos,"explousion"))