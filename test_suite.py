import unittest

import test
import test2

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test)
suite.addTests(loader.loadTestsFromModule(test2))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)


