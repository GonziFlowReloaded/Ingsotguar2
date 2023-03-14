
class Ascensor():

    def __init__(self, piso) -> None:
        self.piso = piso
        self.registro = []
        

    def getPisoActual(self):
        return self.piso
    
    def irA(self, piso):
        if piso<self.piso:
            for i in list(range(self.piso, piso-1, -1)):
                self.registro.append(i)
        else:
            for i in list(range(self.piso, piso+1)):
                self.registro.append(i)
        self.piso = piso

    def verRegistro(self):
        return self.registro
