import abc

class ITimer():
    @abc.abstractmethod
    def get_time(self):
        raise NotImplementedError