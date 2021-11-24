phone = {'brand':'apple', 'model': 11, 'color': 'black', 'storage':'128GB', 'case': True, 'lenses': 3,}

items = phone.items()

for key,value in items:	
	print(f"{key} = {value}")