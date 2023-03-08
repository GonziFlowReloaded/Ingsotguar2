# lista = []
# lista.append("asd")
# print(len(lista))
# palabra = "riquelme"
# print(len(palabra))

import pytest
from carpeta import Carpeta


def testCrearCarpeta():
    miCarpeta = Carpeta("Pepe")
    assert miCarpeta.getNombre == "Pepe"
