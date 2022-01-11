class C:
	def __init__(self, string):
		self.string = string

	def m(self):
		x = 0
		for i in self.string:
			count = self.string.count(i)
			if count > 1:
				x += 1
		if x == 0:
			return True
		else:
			return False

y = C("red sun")
print(y.m())