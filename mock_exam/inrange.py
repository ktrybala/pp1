def inrange(x,y,z):
	numbers = [y,z]
	numbers.sort()
	if numbers[0] <= x <= numbers[1]:
		print("True")
	else:
		print("False")
