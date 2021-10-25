x = int(input("Give the X cordinates: "))
y = int(input("Give the Y cordinates: "))

if (x > 0 and y > 0):
	print("Your cordinates are in first quadrant.")

elif (x > 0 and y < 0):
	print("Your cordinates are in fourth quadrant.")

elif (x < 0 and y > 0):
	print("Your cordinates are in second quadrant.")

elif (x < 0 and y < 0):
	print("Your cordinates are in third quadrant.")

elif (x == 0 and y == 0):
	print("Your cordinates are in (0,0) position.")

