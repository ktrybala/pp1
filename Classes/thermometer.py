class Thermometer:

	def __init__(self):
		self.temp = 0
		self.status = False

	def show_status(self):
		if self.status == True:
			print("Thermometer is on.")
		else:
			print("Thermometer is off.")

	def turn_on(self):
		if self.status == False:
			self.status = True

		elif self.status == True:
			print("Thermometer is already on.")

	def turn_off(self):
		if self.status == True:
			self.status = False

		elif self.status == False:
			print("Thermometer is already off.")

	def measure_temp(self):
		import random

		if self.status == False:
			print("The Thermometer is off.")

		elif self.status == True:
			self.temp = round(random.uniform(34.0, 42.0),1)
			if 41 > self.temp > 37:
				print(f"{self.temp}, FEVER")
			elif self.temp > 42:
				print(f"{self.temp}, CRITICAL TEMPERATURE!!")

			elif self.temp < 37:
				print(self.temp)

