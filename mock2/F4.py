def f4(d):
	suma = 0
	for x,y in d.items():
		for z in y:
			if 10 >= z >= 5:
				suma += z
	return suma
print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))