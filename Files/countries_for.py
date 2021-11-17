f = open('countries.txt','r')
x = 1
for i in f:
	print(f"{x}.", i, end = "")
	x += 1
f.close()
