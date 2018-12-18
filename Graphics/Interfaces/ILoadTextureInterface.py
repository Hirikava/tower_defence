import abc

class ILoadTextureInterface():
    @abc.abstractmethod
    def load(self,filename):
        raise NotImplementedError

    