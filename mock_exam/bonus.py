def bonus(x):
	result = 0
	if x >= 5:
		for i in range(5):
			result += 100
			x -= 1
		if x >= 3:
			for u in range(3):
				result += 200
				x -= 1
			for k in range(x):
				result += 50
				x -= 1
		elif x < 3:
			for u in range(x):
				result += 200
				x -= 1
	elif x < 5:
		for u in range(x):
			result += 100
			x -= 1
	print(result)