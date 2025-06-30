from .request_tests import RequestTests
from .validation_tests import ValidationTests
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add all test classes here
suite.addTests(loader.loadTestsFromTestCase(RequestTests))
suite.addTests(loader.loadTestsFromTestCase(ValidationTests)) # Add other test classes here

# run the tests
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
