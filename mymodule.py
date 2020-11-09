class MyClass:

	def __init__(self, n1, n2):

		self.num1 = n1
		self.num2 = n2

	def get_nums(self):
		return (self.num1, self.num2)

	def always_True(self):
		return True

	def always_False(self):
		return False

	def add_nums(self):
		return self.num1 + self.num2

	def subtract_nums(self):
		return self.num1 - self.num2

	def multiply_nums(self):
		return self.num1 * self.num2

	def divide_nums(self):
		return self.num1 // self.num2
