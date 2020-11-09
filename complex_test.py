import unittest

from Complex import Complex

class ComplexTest(unittest.TestCase):

	def setUp(self):
		unittest.TestCase.setUp(self)
		self.C1 = Complex(1,2)
		self.C2 = Complex(2,3)

	def tearDown(self):
		unittest.TestCase.tearDown(self)
		# self.C1.close()
		# self.C2.close()

	def testAdd(self):
		result = self.C1.add(self.C2)
		self.assertEqual(result.get_r(), 3)
		self.assertEqual(result.get_i(), 5)

	def testEqual(self):
		self.assertTrue(not self.C1.equal(self.C2))
		self.assertTrue(self.C1.equal(Complex(1,2)))

if (__name__ == '__main__'):
	unittest.main()

