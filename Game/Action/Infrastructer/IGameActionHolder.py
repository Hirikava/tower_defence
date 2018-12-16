import abc

class IGameActionHolder():
    @abc.abstractmethod
    def get_actions(self):
        raise NotImplementedError


