from cElementoBase import ElementoBase
class Tijera(ElementoBase):
    def __init__(self):
        super().__init__("Tijera")
    
    def ganar(self, otroElemento):
        return otroElemento.ganaTijera()
    
    def ganaTijera(self):
        return "Empata"
    def ganaPapel(self):
        return "Pierde"
    def ganaPiedra(self):
        return "Gana"
    