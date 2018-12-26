from UserInterface.IUIAction import IUIAction
from UserInterface.IUIActionHolder import IUIActionHolder


class Button(IUIActionHolder):
    def __init__(self,UIAction,cords,shape,name):
        self.cords = cords
        self.shape = shape
        self.action = UIAction
        self.name = name

    def get_actions(self):
        return self.action

    def on_click(self,cords):
        return cords[0] >= self.cords[0] and cords[0] <= self.cords[0] + self.shape[0] and cords[1] >= self.cords[1] and cords[1] <= self.cords[1] + self.shape[1]
