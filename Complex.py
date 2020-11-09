class Complex:

	real_part = 0
	imaginary_part = 0

	def __init__(self, r, l):
		self.real_part = r
		self.imaginary_part = l

	def equal(self, C):
		return (self.real_part==C.get_r() and self.imaginary_part==C.get_i())

	def add(self, C):
		return Complex(self.real_part+C.get_r(), self.imaginary_part+C.get_i())

	def get_r(self):
		return self.real_part

	def get_i(self):
		return self.imaginary_part