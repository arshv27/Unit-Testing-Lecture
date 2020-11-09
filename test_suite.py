import unittest

import test_assertions
import complex_test

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_assertions)
suite.addTests(loader.loadTestsFromModule(complex_test))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)


