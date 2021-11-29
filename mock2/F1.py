def f1(a):
	x = 0
	for i in a:
		if i > 8 and i % 2 == 0:
			x += 1
	return x
print(f1([13,7,4,16,3,12,8,10,20,30,40,50]))
