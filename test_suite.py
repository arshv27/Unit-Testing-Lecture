import unittest

import test_assertions
import test_complex

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_assertions)
suite.addTests(loader.loadTestsFromModule(test_complex))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)


