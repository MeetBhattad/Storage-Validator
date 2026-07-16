class Storage:

    def __init__(self, size):
        self.size = size
        self.memory = {}

        for block in range(size):
            self.memory[block] = ""

    def _validate_block(self, block):
        if block not in self.memory:
            raise ValueError(f"Block {block} does not exist.")

    def write(self, block, data):
        self._validate_block(block)
        
        self.memory[block] = data

    def read(self, block):
        self._validate_block(block)
        
        return self.memory[block]
    
    def delete(self, block):
        self._validate_block(block)
        
        self.memory[block] = ""