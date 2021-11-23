with open("integers.txt", "w") as f:
	for i in range(1,51):
		x = str(i)
		f.write(x + "\n")