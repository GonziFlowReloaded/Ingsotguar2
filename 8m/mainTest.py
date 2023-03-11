from archivo import Archivo
from carpeta import Carpeta
from foto import Foto


def testCrearCarpeta():
    miCarpeta = Carpeta("Pepe")
    assert miCarpeta.getNombre() == "Pepe"

def testCarpetaCambiarNombre():
    miCarpeta = Carpeta("Pepe")
    miCarpeta.setNombre("Juan")
    assert miCarpeta.getNombre() == "Juan"

def test_DebeCrearUnArchivo():
    miArchivo = Archivo("archivo1.txt")
    assert miArchivo.getNombre() == "archivo1.txt"

def test_DebeCrearUnaFoto():
    miFoto = Foto("foto1.jpg", "300x300")
    assert miFoto.getNombre() == "foto1.jpg"


def test_DebeInsertarFotoEnCarpeta():
    miCarpeta = Carpeta("Carpeta1")
    miFoto = Foto("foto1.jpg", "300x300")
    miCarpeta.addElemento(miFoto)
    assert miCarpeta.contarElementos() == 1

def test_DebeInsertarArchivoEnCarpeta():
    miCarpeta = Carpeta("Carpeta1")
    miArchivo = Archivo("archivo1.txt")
    miCarpeta.addElemento(miArchivo)
    assert miCarpeta.contarElementos() == 1

def test_DebeInsertarFotoYArchivoEnCarpeta():
    miCarpeta = Carpeta("Carpeta1")
    miFoto = Foto("foto1.jpg", "300x300")
    miArchivo = Archivo("archivo1.txt")
    miCarpeta.addElemento(miFoto)
    miCarpeta.addElemento(miArchivo)
    assert miCarpeta.contarElementos() == 2
    # elementos = miCarpeta.getElementos()
    # assert elementos[0].getNombre() == "foto1.jpg"

def test_DebeInsertarUnaCarpetaDentroDeOtra():
    miCarpeta = Carpeta("Carpeta1")
    miCarpeta2 = Carpeta("Carpeta2")
    miCarpeta.addElemento(miCarpeta2)
    assert miCarpeta.contarElementos() == 1
    assert miCarpeta.getElementos()[0].getNombre() == "Carpeta2"


def test_DebeInsertarUnaCarpetaDentroDeOtraConUnArchivo():
    miCarpeta = Carpeta("Carpeta1")
    miCarpeta2 = Carpeta("Carpeta2")
    miArchivo = Archivo("archivo1.txt")
    miCarpeta2.addElemento(miArchivo)
    miCarpeta.addElemento(miCarpeta2)
    assert miCarpeta.contarElementos() == 1
    assert miCarpeta.getElementos()[0].getNombre() == "Carpeta2"
    assert miCarpeta.getElementos()[0].getElementos()[0].getNombre() == "archivo1.txt"