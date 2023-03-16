import cPapel
import cPiedra
import cTijera


# -------------------------------------------------- #
# --------------------Piedra------------------------ #

def test_PiedraVsTijera():
    piedra = cPiedra.Piedra()
    tijera = cTijera.Tijera()
    assert piedra.ganar(tijera) == "Gana"

def test_PiedraVsPapel():
    piedra = cPiedra.Piedra()
    papel = cPapel.Papel()
    assert piedra.ganar(papel) == "Pierde"

def test_PiedraVsPiedra():
    piedra = cPiedra.Piedra()
    piedra2 = cPiedra.Piedra()
    assert piedra.ganar(piedra2) == "Empata"

# -------------------------------------------------- #
# --------------------Papel------------------------- #

def test_PapelVsPiedra():
    papel = cPapel.Papel()
    piedra = cPiedra.Piedra()
    assert papel.ganar(piedra) == "Gana"

def test_PapelVsTijera():
    papel = cPapel.Papel()
    tijera = cTijera.Tijera()
    assert papel.ganar(tijera) == "Pierde"

def test_PapelVsPapel():
    papel = cPapel.Papel()
    papel2 = cPapel.Papel()
    assert papel.ganar(papel2) == "Empata"

# -------------------------------------------------- #
# --------------------Tijera------------------------ #
def test_TijeraVsPapel():
    tijera = cTijera.Tijera()
    papel = cPapel.Papel()
    assert tijera.ganar(papel) == "Gana"


def test_TijeraVsPiedra():
    tijera = cTijera.Tijera()
    piedra = cPiedra.Piedra()
    assert tijera.ganar(piedra) == "Pierde"

def test_TijeraVsTijera():
    tijera = cTijera.Tijera()
    tijera2 = cTijera.Tijera()
    assert tijera.ganar(tijera2) == "Empata"


