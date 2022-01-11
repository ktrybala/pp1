class C:
	def __init__(self, tab):
		self.tab = tab

	def m(self):
		x = 0
		y = 2
		z = 0

		for i in self.tab:
			try:
				if self.tab[x] == self.tab[y]:
					z += 1
					x += 1
					y += 1
				else:
					x += 1
					y += 1
			except IndexError:
				pass

		return z

print(C([True,False,True,True,False,True,False,True,False,True]).m())
