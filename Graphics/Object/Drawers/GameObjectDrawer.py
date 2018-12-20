from Graphics.Object.Drawers.DrawAction import CreatureDrawAction, TowerDrawAction, ProjectileDrawAction
from Graphics.Object.Infrastructure.IGraphicsActionHolder import IGraphicsActionHolder


class GameObjectDrawer(IGraphicsActionHolder):
    def __init__(self,game_session):
        self.game_session = game_session

    def get_actions(self):
        args = self.game_session.get_args()
        actions = []
        for target in args[1]:
            actions.append(CreatureDrawAction(target))
        for target in args[2]:
            actions.append(TowerDrawAction(target))
        for target in args[5]:
            actions.append(ProjectileDrawAction(target))
        return actions