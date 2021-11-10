def month(n):
	tab = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	return tab[n-1]
	
n = int(input("Give the month number: "))

print(f"Month name: {month(n)}")
