array = [4, 3, 7, 1, 3]
sum1 = 0

def sum(array,sum1):
	for x in array:
		sum1 += x
	return sum1

def array2str(array):
	result = ""
	for x in array:
		result += " " + str(x)
	return result

print (array)
print(f"Sum of the array numbers: {sum(array,sum1)}")
print(array2str(array))

