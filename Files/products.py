with open("MeatAndFish.txt", "r") as f:
	content = f.read() + "\n"

with open("GrainsAndBread.txt", "r") as f:
	content += f.read()

with open("products.txt", "w") as f:
	f.write(content)