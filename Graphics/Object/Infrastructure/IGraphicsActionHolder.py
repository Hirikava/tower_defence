import abc
class IGraphicsActionHolder():

    @abc.abstractmethod
    def get_actions(self):
        raise NotImplementedError