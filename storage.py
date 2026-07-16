from logger import logger

class Storage:

    def __init__(self, size):
        self.size = size
        self.memory = {}

        for block in range(size):
            self.memory[block] = ""

    def _validate_block(self, block):
        if block not in self.memory:

            logger.error(
                f"Attempted access to invalid Block {block}"
            )
            
            raise ValueError(f"Block {block} does not exist.")

    def write(self, block, data):
        self._validate_block(block)

        if not isinstance(data, str):
            raise TypeError("Only string is allowed")
        
        self.memory[block] = data

        logger.info(
            f'Wrote "{data}" to Block {block}'
        )

    def read(self, block):
        self._validate_block(block)
        
        data = self.memory[block]

        logger.info(
            f'Read "{data}" from Block {block}'
        )
        return data
    
    def delete(self, block):
        self._validate_block(block)
        
        self.memory[block] = ""

        logger.info(
            f"Deleted data from Block {block}"
        )