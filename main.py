from storage import Storage
from validator import Validator

storage = Storage(5)
validator = Validator()
storage.write(2, "Hello")
expected = "Hello"
actual = storage.read(2)

if validator.validate(expected, actual):
    print("PASS")
else:
    print("FAIL")