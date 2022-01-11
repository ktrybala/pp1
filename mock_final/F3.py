class C:
	def __init__(self, tab):
		self.tab = tab
	def m(self):
		x = 0
		y = 0
		tab2 = []
		for i in self.tab:
			tab2.append(i.lower())
			for a in tab2:
				count = tab2.count(a)
				if count != 1:
					y += 1
		if y != 0:
			return True
		else:
			return False