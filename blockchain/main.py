import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calcular el hash del bloque actual utilizando los datos del bloque y el hash del bloque anterior
        return hashlib.sha256((str(self.data) + str(self.previous_hash)).encode('utf-8')).hexdigest()

    def __str__(self):
        return f"Block [data={self.data}, hash={self.hash}, previous_hash={self.previous_hash}]"

class Blockchain:
    def __init__(self):
        self.blocks = [Block("Genesis Block", None)]
        self.memento = None

    def add_block(self, data):
        # Crear un nuevo bloque y agregarlo a la cadena de bloques
        previous_block = self.blocks[-1]
        new_block = Block(data, previous_block.hash)
        self.blocks.append(new_block)

    def get_last_block(self):
        # Devuelve el último bloque de la cadena de bloques
        return self.blocks[-1]

    def save(self):
        # Crear un memento con la cadena de bloques actual
        self.memento = BlockchainMemento(self.blocks)

    def restore(self):
        # Restaurar la cadena de bloques desde el memento
        self.blocks = self.memento.get_blocks()

    def __str__(self):
        # Devuelve una cadena que representa toda la cadena de bloques
        return "\n".join([str(block) for block in self.blocks])

class BlockchainMemento:
    def __init__(self, blocks):
        # Guarda una copia de la cadena de bloques actual
        self.blocks = [Block(block.data, block.previous_hash) for block in blocks]

    def get_blocks(self):
        # Devuelve una copia de la cadena de bloques
        return [Block(block.data, block.previous_hash) for block in self.blocks]
