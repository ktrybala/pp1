
y = 0

with open("lorem.txt", "r") as f:
	for i in f:
		print(i, end = '')
		y += 1
		if y % 5 == 0:
			x = str(input(""))
			if x == "":
				continue

