from Graphics.Object.Drawers.DrawAction import DrawButtonAction, DrawObserverAction
from Graphics.Object.Infrastructure.IGraphicsActionHolder import IGraphicsActionHolder


class UIObjectDrawer(IGraphicsActionHolder):
    def __init__(self,ui_session):
        self.ui = ui_session

    def get_actions(self):
        actions = []
        for button in self.ui.get_button_set():
            actions.append(DrawButtonAction(button))
        actions.append(DrawObserverAction(self.ui.observer))
        return actions
