class Elemento():

    def __init__(self, nombre):
        self.nombre = nombre
        self.tamaño = len(nombre)

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre