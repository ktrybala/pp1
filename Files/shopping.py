with open("shopping_list.txt","a") as f:
	while True:
		x = input("Add product (type 0 to leave): ")
		if x == str(0) : break
		f.write(x + "\n")
