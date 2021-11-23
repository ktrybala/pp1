with open("powers.txt", "w") as f:
	for i in range (1,11):
		n1 = str(i)
		n2 = str(i**2)
		n3 = str(i**3)
		f.write(f"{n1}, {n2}, {n3}\n")