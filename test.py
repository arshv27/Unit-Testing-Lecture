import unittest

class MyTest(unittest.TestCase):

	def test_Subtract(self):
		self.assertEqual(4 - 1, 3, "4 - 1 not equal to 3")

	def test_Divide(self):
		self.assertEqual(6 // 2, 3, "6 // 2 not equal to 3")

if __name__ == '__main__':
	unittest.main()