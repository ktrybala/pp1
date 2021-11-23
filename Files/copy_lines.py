lines = []
with open("lorem.txt", "r") as f:
	for i in f:
		lines.append(i)

with open("copylines.txt", "w") as f:
	for y in range(len(lines)):
		f.write(lines[y])
