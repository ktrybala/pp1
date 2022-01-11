class C:
	def __init__(self, dict1):
		self.dict1 = dict1
		self.system = dict1["system"]
		self.value = dict1["value"]

	def m(self):
		x = 0
		liczba = 0
		if self.system == "2":
			for i in self.value:
				print(i)
				if i != "0" and i!= "1":
					return -1
				else:
					liczba = int(self.value, 2)
					return liczba
		elif self.system == "8":
			pass
		elif self.system == "16":
			pass


print(C({"system":"2", "value":"101"}).m())
