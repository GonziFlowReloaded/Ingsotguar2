from elemento import Elemento

class Carpeta(Elemento):
    
    def __init__(self, nombre):
        super(nombre)
        self.elementos = list
    

    def addElemento(self, element):
        self.elementos.append(element)

    def contarElementos(self):
        return(len(self.elementos))
    
    def getElementos(self):
        return self.elementos()
    

    