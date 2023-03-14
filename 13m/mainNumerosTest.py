from ascensor import Ascensor
from piso import Piso

def test_DebeCrearAscensor():
    ascensor1 = Ascensor(1)
    assert ascensor1.getPisoActual() == 1

def test_DebeIrAUnPiso():
    ascensor1 = Ascensor(1)
    ascensor1.irA(3)
    assert ascensor1.getPisoActual() == 3
    assert ascensor1.verRegistro()[1] == 2

def test_DebeIr01():
    ascensor1 = Ascensor(0)
    ascensor1.irA(1)
    arregloEsperado = [0,1]
    assert arregloEsperado == ascensor1.verRegistro()

def test_DebeIr05():
    ascensor1 = Ascensor(0)
    ascensor1.irA(5)
    arregloEsperado = [0,1,2,3,4,5]
    assert arregloEsperado == ascensor1.verRegistro()

def test_DebeIr03322():
    ascensor1 = Ascensor(0)
    ascensor1.irA(3)
    ascensor1.irA(2)
    ascensor1.irA(2)
    arregloEsperado = [0,1,2,3,3,2,2]
    assert arregloEsperado == ascensor1.verRegistro()
    
def test_DebeIr054():
    ascensor1 = Ascensor(0)
    ascensor1.irA(5)
    ascensor1.irA(4)
    arregloEsperado = [0,1,2,3,4,5,5,4]
    assert arregloEsperado == ascensor1.verRegistro()
    