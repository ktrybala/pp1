import re

def f3(t):
	x = 0
	y = 0
	tab = re.findall(r"\b\d{2,3}\b",t)
	for i in tab:
		y = int(i)
		x += y
	return x

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))