import re

with open("grades.txt", "r") as f:
	content = f.read()
grades = re.findall("\d.\d", content)
suma = 0

for i in grades:
	x = float(i)
	suma += x

mean = suma / len(grades)

print(round(mean,2))