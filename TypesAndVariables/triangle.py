import math

a = int(input("Value of the first side: "))
b = int(input("Value of the second side: "))
c = int(input("Value of the third side: "))

sides = [a,b,c]
sides.sort() #sorting sides by theirs value

def heron():
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print(f"Area of the triangle: {round(area,2)}")

if (sides[0] + sides[1]) > sides[2]:
	heron()
else:
	print("Change values of triangle sides, they do not meet the criterias of triangle inequlity.")
