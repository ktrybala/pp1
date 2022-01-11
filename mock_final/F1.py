class C:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		a = self.name[0]
		b = self.surname[0]
		a = a.capitalize()
		b = b.capitalize()
		print(a+b)

x = C("anna", "may")