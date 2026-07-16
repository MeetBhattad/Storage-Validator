import unittest
import time

from test_storage import TestStorage

start_time = time.time()

suite = unittest.TestLoader().loadTestsFromTestCase(TestStorage)

runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)

end_time = time.time()

passed = result.testsRun - len(result.failures) - len(result.errors)
failed = len(result.failures)
errors = len(result.errors)

report = f"""
=============================
 Storage Validation Report
=============================

Total Tests : {result.testsRun}

Passed      : {passed}

Failed      : {failed}

Errors      : {errors}

Execution Time : {end_time-start_time:.4f} seconds

=============================
"""

print(report)

with open("report.txt", "w") as file:
    file.write(report)