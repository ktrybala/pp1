f = open("integers.txt","r")
sum1 = 0
for i in f:
	sum1 += int(i)
f.close()
print(sum1)
