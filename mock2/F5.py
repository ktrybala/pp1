def f5(c):
	counter = 0
	with open("poem.txt","r") as f:
		for i in f:
			if c in i:
				counter += 1
	return counter
print(f5("m"))