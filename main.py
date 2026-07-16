from storage import Storage

storage = Storage(5)
storage.write(2, "Hello")
print(storage.read(2))
storage.delete(2)
print(storage.read(2))