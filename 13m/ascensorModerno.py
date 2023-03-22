from piso import Piso

class AscensorModerno():

    def __init__(self, piso) -> None:
        self.piso = piso
        self.registro = []
        
    def getPisoActual(self):
        return self.piso
    
    

    def verHistorial(self):
        return self.registro
    
    def verHistorialString(self):
        lista = []
        for piso in self.registro:
            lista.append(piso.getNombre())
        return lista

    def setPiso(self, piso):
        self.piso = piso
    
    def __bajarHasta__(self, piso):
        pisoActual = self.getPisoActual()
        historial = []
        while pisoActual != piso and pisoActual != None:
            historial.append(pisoActual)
            pisoActual = pisoActual.getPisoAbajo()
        if pisoActual == piso:
            historial.append(pisoActual)
        if pisoActual == None:
            historial = []
        return historial

    def __subirHasta__(self, piso):
        pisoActual = self.getPisoActual()
        historial = []
        while pisoActual != piso and pisoActual != None:
            historial.append(pisoActual)
            pisoActual = pisoActual.getPisoArriba()
        if pisoActual == piso:
            historial.append(pisoActual)
        if pisoActual == None:
            historial = []
        return historial
    def irA(self, piso):
        
        if self.__subirHasta__(piso) != []:
            self.registro.extend(self.__subirHasta__(piso))
            self.setPiso(piso)
        elif self.__bajarHasta__(piso) != []:
            self.registro.extend(self.__bajarHasta__(piso))
            self.setPiso(piso)
        else:
            return None
        
        

    