import unittest

class MyTest(unittest.TestCase):

	def test_Add(self):
		self.assertEqual(1 + 2, 3, "1 + 2 not equal to 3")

	def test_Multiply(self):
		self.assertEqual(2 * 3, 6, "2 * 3 not equal to 6")

if __name__ == '__main__':
	unittest.main()
