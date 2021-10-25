def first():
	global result
	result = age * 10.5
	print(f"The dogs age in dog's years is {result} years.")

def second():
	global result2
	global rest
	rest = age - 2
	result2 = (2 * 10.5) + (rest * 4)
	print(f"The dogs age in dog's years is {result2} years.")
age = float(input("Enter dog's age in human years: "))

if age <=2:
	first()

elif age > 2:
	second()

else:
	print("Invalid input")
	