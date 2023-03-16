
from cElementoBase import ElementoBase

class Piedra(ElementoBase):
    def __init__(self):
        super().__init__("Piedra")
        
    def ganar(self, otroElemento):
        return otroElemento.ganaPiedra()

    def ganaPapel(self):
        return "Gana"
    
    def ganaTijera(self):
        return "Pierde"
    
    def ganaPiedra(self):
        return "Empata"