import hashlib
from main import Block, Blockchain, BlockchainMemento

def test_calculate_hash():
    # Test para verificar que el cálculo del hash se realiza correctamente
    block = Block("test_data", "test_previous_hash")
    assert block.calculate_hash() == hashlib.sha256("test_data".encode('utf-8') + "test_previous_hash".encode('utf-8')).hexdigest()


def test_add_block():
    # Test para verificar que se agrega correctamente un bloque a la cadena
    blockchain = Blockchain()
    blockchain.add_block("test_data")
    assert len(blockchain.blocks) == 2

def test_get_last_block():
    # Test para verificar que se obtiene correctamente el último bloque de la cadena
    blockchain = Blockchain()
    blockchain.add_block("test_data")
    last_block = blockchain.get_last_block()
    assert last_block.data == "test_data"

def test_save_and_restore():
    # Test para verificar que se guarda y restaura correctamente la cadena de bloques
    blockchain = Blockchain()
    blockchain.add_block("test_data1")
    blockchain.save()
    blockchain.add_block("test_data2")
    blockchain.restore()
    assert len(blockchain.blocks) == 2
    assert blockchain.get_last_block().data == "test_data1"

def test_block_str():
    # Test para verificar que la representación en string de un bloque es correcta
    block = Block("test_data", "test_previous_hash")
    assert str(block) == "Block [data=test_data, hash=" + block.calculate_hash() + ", previous_hash=test_previous_hash]"

def test_save_and_restore2():
    # Test para verificar que se guarda y restaura correctamente la cadena de bloques
    blockchain = Blockchain()
    blockchain.add_block("Testeo1")
    blockchain.save()
    blockchain.add_block("Testeo2")
    blockchain.save()
    blockchain.add_block("Testeo3")
    blockchain.restore()
    assert len(blockchain.blocks) == 3
    assert blockchain.get_last_block().data == "Testeo2"