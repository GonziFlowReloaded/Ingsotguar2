from ascensorModerno import AscensorModerno
from piso import Piso

def test_DebeIrAlPisoE():
    piso1 = Piso("Planta A")
    piso2 = Piso("Planta B")
    piso3 = Piso("Planta C")
    piso4 = Piso("Planta D")
    piso5 = Piso("Planta E")

    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(piso1)
    ascensor1.irA(piso5)
    
    listaEsperada = ['Planta A', ['Planta B', 'Planta C', 'Planta D', 'Planta E']]
    assert listaEsperada == ascensor1.verHistorial()
