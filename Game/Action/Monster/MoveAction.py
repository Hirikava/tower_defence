from Game.Action.Infrastructer.IGameAction import IGameAction


class MoveAction(IGameAction):
    def __init__(self,tracked_monster):
        self.__target__ = tracked_monster

    def act(self,*args):
        if self.__target__.track_counter == len(self.__target__.track):
            return True
        if self.__target__.move_to(self.__target__.track[self.__target__.track_counter],args[0]):
            self.__target__.track_counter += 1