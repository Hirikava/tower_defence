import abc

class IClock():
    @abc.abstractmethod
    def tick(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_time(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delay(self,time_span):
        raise NotImplementedError
