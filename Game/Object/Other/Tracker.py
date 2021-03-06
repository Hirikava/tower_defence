
class Tracker():
    def __init__(self):
        self.__set__ = set()

    def add(self,element):
        self.__set__.add(element)

    def contains(self,element):
        return self.__set__.__contains__(element)

    def remove(self,element):
        self.__set__.remove(element)

    def __iter__(self):
        set = self.__set__.copy()
        return  set.__iter__()