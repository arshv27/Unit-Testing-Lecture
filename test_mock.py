# import unittest
# from mock_class import MyClass

# class MockDataSource(object):
# 	def __init__(self):
# 		self.readFrom = False
# 		self.closed = False

# 	def read(self):
# 		self.readFrom = True
# 		return 'some data'

# 	def close(self):
# 		self.closed = True


# class TestMyClass(unittest.TestCase):

# 	def testConstructor(self):
# 		"Test the default state"
# 		myclass = MyClass()

# 		self.assertEqual(myclass.data, None)

# 	def testReadData(self):
# 		myclass = MyClass()

# 		source = MockDataSource()

# 		myclass.readData(source)

# 		self.assertEqual(myclass.data, 'some data')
# 		self.assertTrue(source.readFrom)
# 		self.assertTrue(source.closed)

# if (__name__ == '__main__'):
# 	unittest.main()


import unittest
from mock import Mock

from mock_class import MyClass

class TestMyClass(unittest.TestCase):

	def testConstructor(self):
		"Test the default state"
		myclass = MyClass()

		self.assertEqual(myclass.data, None)

	def testReadData(self):
		myclass = MyClass()

		source = Mock()
		source.read.return_value = 'some data'

		myclass.readData(source)

		self.assertEqual(myclass.data, 'some data')
		self.assertTrue(source.read.called)
		self.assertTrue(source.close.called)

if (__name__ == '__main__'):
	unittest.main()
