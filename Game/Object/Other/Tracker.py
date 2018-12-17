
class Tracker():
    def __init__(self):
        self.__set__ = set()

    def add(self,element):
        self.__set__.add(element)

    def remove(self,element):
        self.__set__.remove(element)

    def __iter__(self):
        return self.__set__.__iter__()