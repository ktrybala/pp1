class C:
	def m(n1,n2):
		import json

		with open("mockdata.json", 'r') as f:
			content = json.load(f)
			count = 0
			for item in content:
				if item['wife']['age'] >= n1 and len(item['children']) >= n2:
					count += 1
			return count

	def m2(n1):
		x = 0
		import json
		f = open("mockdata1.json","w")
		f2 = open("mockdata.json","r")
		x = json.load(f2)
		for i in x:
			if len(i['children']) >= n1:
				json.dump(i,f, indent = 3)
		f.close()
		f2.close()

print(C.m(10,2))
print(C.m2(2))