import unittest

from mymodule import MyClass

class MyTest(unittest.TestCase):

	def setUp(self):
		unittest.TestCase.setUp(self)

		self.myclass = MyClass(2, 2)

	def tearDown(self):
		unittest.TestCase.tearDown(self)

		del(self.myclass)

	def testTrue(self):
		result = self.myclass.always_True()
		self.assertTrue(result)


	def testFalse(self):
		result = self.myclass.always_False()
		self.assertFalse(result)


	def testEqual(self):
		first = self.myclass.add_nums()
		second = self.myclass.multiply_nums()

		self.assertEqual(first, second)


	def testNotEqual(self):
		third = self.myclass.subtract_nums()
		fourth = self.myclass.divide_nums()

		self.assertNotEqual(third, fourth)


if (__name__ == '__main__'):
	unittest.main()
