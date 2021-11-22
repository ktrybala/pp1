from os.path import exists

name = str(input("Give the file's directory or its name (if it's inside Files folder): "))
x = 0

y = exists(name)

if y == True:
    with open(f"{name}", "r") as f:
	    for i in f:
		    x += 1
    print(f"This text file has {x} lines.")
else:
	print("This file doesn't exists")
