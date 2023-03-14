from piso import Piso

class AscensorModerno():

    def __init__(self, piso) -> None:
        self.piso = piso
        self.registro = []
        
    def getPisoActual(self):
        return self.piso
    
    def irA(self, piso):
        a = 0
        self.registro.append(self.piso.obtenerPiso())
        pisos = []

        while self.piso.getPisoArriba() != None:
            if self.getPisoActual() == piso:
                a = 0
                break
            if self.getPisoActual() == None:
                self.piso = self.piso.getPisoAbajo()
                a = 1
                break
            self.piso = self.piso.getPisoArriba()
            pisos.append(self.piso.obtenerPiso())
        
        if a == 1:
            pisos = []
            while self.piso.getPisoAbajo() != None:
                if self.getPisoActual() == piso:
                    break
                if self.getPisoActual() == None:
                    self.piso = self.piso.getPisoArriba()
                    break
                self.piso = self.piso.getPisoAbajo()
                pisos.append(self.piso.obtenerPiso())
        
        if a == 0:
            self.registro.append(pisos)
        else:
            self.registro.append(pisos)

    def verHistorial(self):
        return self.registro

    
    