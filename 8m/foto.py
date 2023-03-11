from elemento import Elemento
class Foto(Elemento):
    def __init__(self, nombre,dimension):
        super().__init__(nombre)
        self.dimension = dimension
    
    def getDimension(self):
        return self.dimension