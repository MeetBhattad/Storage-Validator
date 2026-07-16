import unittest
from storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage(5)

    def test_write(self):
        self.storage.write(2, "Hello")

        self.assertEqual(
            self.storage.read(2),
            "Hello"
        )

    def test_delete(self):
        self.storage.write(1, "Python")
        self.storage.delete(1)

        self.assertEqual(
            self.storage.read(1),
            ""
        )
    
    def test_invalid_block(self):
        with self.assertRaises(ValueError):
            self.storage.read(10)

    def test_overwrite(self):
        self.storage.write(2, "Hello")
        self.storage.write(2, "World")

        self.assertEqual(
            self.storage.read(2),
            "World"
        )

    def test_empty_block(self):
        self.assertEqual(
            self.storage.read(3),
            ""
        )

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.storage.write(1, 12345)
    

if __name__ == "__main__":
    unittest.main()