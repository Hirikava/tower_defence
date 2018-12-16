import abc

class IGameObject():
    @abc.abstractmethod
    def get_cords(self):
        raise NotImplementedError