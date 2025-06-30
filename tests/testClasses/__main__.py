import unittest
import sys

from .request_tests import RequestTests
from .validation_tests import ValidationTests

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add all test classes here
suite.addTests(loader.loadTestsFromTestCase(RequestTests))
suite.addTests(loader.loadTestsFromTestCase(ValidationTests))

# run the tests
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# return error code 1 on failure
if not result.wasSuccessful():
    sys.exit(1)
sys.exit(0)
