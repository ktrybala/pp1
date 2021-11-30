import csv
def f6(g,n1,n2):
	x = 0
	with open("people.csv","r") as f:
		content = csv.reader(f)
		next(content)
		for row in content:
			h = int(row[2])
			if row[3] == g and n1 <= h <= n2:
				x += 1
	return x
print(f6("Female",160,180))