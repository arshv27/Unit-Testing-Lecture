# import unittest

# from mymodule import MyClass

# class MyTest(unittest.TestCase):

# 	def testTrue(self):
# 		myclass = MyClass(2, 2)

# 		try:
# 			result = myclass.always_True()
# 			self.asssertTrue(result)

# 		finally:
# 			myclass.close()


# 	def testFalse(self):
# 		myclass = MyClass(2, 2)

# 		try:
# 			result = myclass.always_False()
# 			self.asssertFalse(result)

# 		finally:
# 			myclass.close()


# 	def testEqual(self):
# 		myclass = MyClass(2, 2)

# 		try:
# 			first = myclass.add_nums()
# 			second = myclass.multiply_nums()

# 			self.assertEqual(first, second)

# 		finally:
# 			myclass.close()


# 	def testNotEqual(self):
# 		myclass = MyClass(2, 2)

# 		try:
# 			third = myclass.subtract_nums()
# 			fourth = myclass.divide_nums()

# 			self.assertNotEqual(third, fourth)

# 		finally:
# 			myclass.close()


import unittest

from mymodule import MyClass

class MyTest(unittest.TestCase):

	def setUp(self):
		unittest.TestCase.setUp(self)

		self.myclass = MyClass(2, 2)

	def tearDown(self):
		unittest.TestCase.tearDown(self)

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

	