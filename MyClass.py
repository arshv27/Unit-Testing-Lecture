class MyClass():
	def __init__(self):
		self.data = None

	def readData(self, source):
		self.data = source.read()
		source.close()