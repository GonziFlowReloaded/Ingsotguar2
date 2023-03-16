import abc

class ElementoBase():
    def __init__(self, nombre):
        self.nombre = nombre
    @abc.abstractmethod
    def ganar(self, elemento):
        pass
    @abc.abstractmethod
    def ganaTijera(self):
        pass
    @abc.abstractmethod
    def ganaPapel(self):
        pass
    @abc.abstractmethod
    def ganaPiedra(self):
        pass