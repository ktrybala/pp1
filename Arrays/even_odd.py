tab = [15, 8, 31, 47, 2, 19]
e = 0
o = 0
for x in tab:
	if x % 2 == 0:
		e += 1
	else:
		o += 1
print(tab)
print(f"Even numbers: {e}, Odd numbers: {o}")