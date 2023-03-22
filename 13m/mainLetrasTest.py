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
    
    listaEsperada = ['Planta A', 'Planta B', 'Planta C', 'Planta D', 'Planta E']
    assert listaEsperada == ascensor1.verHistorialString()


def test_DebeIrAlPisoA():
    piso1 = Piso("Planta A")
    piso2 = Piso("Planta B")
    piso3 = Piso("Planta C")
    piso4 = Piso("Planta D")
    piso5 = Piso("Planta E")

    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(piso5)
    ascensor1.irA(piso1)
    
    listaEsperada = ['Planta E', 'Planta D', 'Planta C', 'Planta B', 'Planta A']
    assert listaEsperada == ascensor1.verHistorialString()

def test_DebeIr01():
    pb = Piso("Planta Baja")
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    pb.setPisoArriba(piso1)
    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(pb)
    ascensor1.irA(piso1)

    listaEsperada = ['Planta Baja', 'Piso 1']
    assert listaEsperada == ascensor1.verHistorialString()

def test_DebeIr05():
    pb = Piso("Planta Baja")
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    pb.setPisoArriba(piso1)
    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(pb)
    ascensor1.irA(piso5)

    listaEsperada = ['Planta Baja', 'Piso 1', 'Piso 2', 'Piso 3', 'Piso 4', 'Piso 5']
    assert listaEsperada == ascensor1.verHistorialString()

def test_DebeIr03322():

    pb = Piso("Planta Baja")
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    pb.setPisoArriba(piso1)
    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(pb)
    ascensor1.irA(piso3)
    ascensor1.irA(piso2)
    ascensor1.irA(piso2)

    listaEsperada = ['Planta Baja', 'Piso 1']
    # assert listaEsperada == ascensor1.verHistorialString()

def test_DebeIr054():
    
    pb = Piso("Planta Baja")
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    pb.setPisoArriba(piso1)
    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensor1 = AscensorModerno(pb)
    ascensor1.irA(piso5)
    ascensor1.irA(piso4)
    
    listaEsperada = ['Planta Baja', 'Piso 1', 'Piso 2', 'Piso 3', 'Piso 4', 'Piso 5', 'Piso 5', 'Piso 4']
    assert listaEsperada == ascensor1.verHistorialString()

