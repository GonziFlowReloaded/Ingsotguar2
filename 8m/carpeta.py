from elemento import Elemento

class Carpeta(Elemento):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []
    

    def addElemento(self, element):
        self.elementos.append(element)

    def contarElementos(self):
        return(len(self.elementos))
    
    def getElementos(self):
        return(self.elementos)
    

    