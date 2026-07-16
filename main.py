from storage import Storage
from validator import Validator
import subprocess

storage = Storage(10)
validator = Validator()
while True:
    print("\n===== STORAGE VALIDATOR =====")
    print("1. Write Data")
    print("2. Read Data")
    print("3. Delete Data")
    print("4. Run Validation Tests")
    print("5. Show Storage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        block = int(input("Enter Block Number: "))

        data = input("Enter Data: ")

        try:
            storage.write(block, data)
            print(f" Successfully wrote data to Block {block}")

        except Exception as e:
            print(e)

    elif choice == "2":

        block = int(input("Enter Block Number: "))

        try:
            data = storage.read(block)
            print(f"Data: {data}")

        except Exception as e:
            print(e)

    elif choice == "3":

        block = int(input("Enter Block Number: "))

        try:
            storage.delete(block)
            print(f" Block {block} cleared")

        except Exception as e:
            print(e)

    elif choice == "4":

        subprocess.run(["python", "test_runner.py"])

    elif choice == "5":

        for block, data in storage.memory.items():

            print(f"Block {block}: '{data}'")

    elif choice == "6":

        print("Exiting...")

        break

    else:
        print("Invalid Choice")


storage.write(2, "Hello")
expected = "Hello"
actual = storage.read(2)

if validator.validate(expected, actual):
    print("PASS")
else:
    print("FAIL")