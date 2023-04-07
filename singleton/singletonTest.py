from singleton import User

def test_Usuario1y2sonElMismoObjeto():
    user1 = User('Pepe')
    user2 = User('Juan')
    print(user1.__str__())
    print(user2.__str__())

    assert user1.__str__() == user2.__str__()

test_Usuario1y2sonElMismoObjeto()