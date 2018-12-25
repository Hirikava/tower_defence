import abc

class IUIActionHolder():
    @abc.abstractmethod
    def get_actions(self):
        raise NotImplementedError