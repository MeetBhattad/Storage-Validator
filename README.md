# Storage Validation Framework

A Python-based Storage Validation Framework that simulates the workflow of a storage/SSD validation engineer. The project demonstrates automated testing, storage operation validation, logging, and report generation using Python.

> **Note:** This project is an educational simulation created to understand software validation concepts. It does **not** interface with real SSD hardware or firmware.

---

## Project Overview

Storage validation engineers ensure that storage devices behave correctly under different conditions by executing automated test cases, validating expected results, analyzing failures, and generating reports.

This project simulates that workflow by implementing a simple block storage system along with automated validation tests and logging.

---

## Features

- Simulated block-based storage
- Read, Write, and Delete operations
- Input validation with exception handling
- Automated unit testing using Python's `unittest`
- Validation report generation
- Logging of storage operations and errors
- Interactive Command Line Interface (CLI)
- Object-Oriented Design

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- unittest
- logging
- Git
- GitHub

---

## Project Structure

```
Storage-Validator/
│
├── main.py              # Command Line Interface
├── storage.py           # Storage implementation
├── validator.py         # Validation logic
├── logger.py            # Logging configuration
├── test_storage.py      # Unit test cases
├── test_runner.py       # Executes all tests & generates report
├── README.md
├── .gitignore
```

---

## System Architecture

```
                User
                  │
                  ▼
             main.py (CLI)
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  Storage Class       Test Runner
        │                   │
        ▼                   ▼
 Validator          Automated Tests
        │                   │
        └─────────┬─────────┘
                  ▼
             Report Generation
                  │
                  ▼
            storage.log
            report.txt
```

---

## Features Demonstrated

### Storage Operations

- Write data to storage blocks
- Read data from storage blocks
- Delete stored data
- Validate block numbers
- Validate input data types

### Automated Testing

The project includes automated test cases for:

- Write Operation
- Read Operation
- Delete Operation
- Invalid Block Access
- Invalid Data Type
- Overwrite Existing Data
- Empty Block Validation

All tests are executed automatically using Python's `unittest` framework.

---

## Logging

Every storage operation is logged.

Example:

```
INFO - Wrote "Hello" to Block 2
INFO - Read "Hello" from Block 2
INFO - Deleted data from Block 2
ERROR - Attempted access to invalid Block 20
```

This helps simulate debugging and failure analysis used during storage validation.

---

## Validation Report

Running the test runner generates a validation report similar to:

```
=============================
Storage Validation Report
=============================

Total Tests : 6
Passed      : 6
Failed      : 0
Errors      : 0

Execution Time : 0.002 seconds
=============================
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/MeetBhattad/Storage-Validator.git
```

Move into the project directory

```bash
cd Storage-Validator
```

Run the application

```bash
python main.py
```

---

## Run Automated Tests

```bash
python test_runner.py
```

or

```bash
python test_storage.py
```

---

## Sample CLI

<img width="669" height="654" alt="Screenshot 2026-07-17 003420" src="https://github.com/user-attachments/assets/db5dbb52-38df-4134-9ea2-2b638ec9d835" />


## Concepts Learned

Through this project I gained hands-on experience with:

- Object-Oriented Programming
- Software Validation
- Automated Testing
- Unit Testing
- Exception Handling
- Logging
- Report Generation
- Git & GitHub
- Clean Code Practices
- Refactoring (DRY Principle)

---

## Future Improvements

- Simulate SSD pages and blocks
- Add checksum verification
- Simulate data corruption scenarios
- Export validation reports as HTML/PDF
- Integrate Continuous Integration (GitHub Actions)
- Add Jenkins pipeline support
- Support concurrent storage operations

---

## Author

**Meet Bhattad**

GitHub: https://github.com/MeetBhattad

LinkedIn: *(Add your LinkedIn profile here)*

---

## License

This project is intended for educational and learning purposes.
