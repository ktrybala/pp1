def f2(a1,a2):
	x = 0
	y = 0
	for i in a1:
		if 100 > i > 9 and i < 100 and i % 2 == 0:
			x += 1
	for u in a2:
		if 100 > u > 9 and u % 2 == 0:
			y += 1
	if x == y:
		return True
	else:
		return False
print(f2([23,7,16,34,120, 98],[1,18,79,20,6,111]))