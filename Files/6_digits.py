import re

with open("lorem.txt","r") as f:
	content = f.read()
words = re.findall("\w{6,}", content)
print(len(words))