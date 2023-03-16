from cElementoBase import ElementoBase

class Papel(ElementoBase):
    def __init__(self):
        super().__init__("Papel")

    def ganar(self, otroElemento):
        return otroElemento.ganaPapel()

    def ganaTijera(self):
        return "Gana"
    
    def ganaPiedra(self):
        return "Pierde"
    
    def ganaPapel(self):
        return "Empata"