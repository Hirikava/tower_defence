import abc

class IWindowProvider():
    @abc.abstractmethod
    def get_window(self):
        raise NotImplementedError