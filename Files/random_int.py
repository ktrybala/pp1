import random
with open("random.txt", "w") as f:
    for i in range(1,51):
	    x = random.randint(100,999)
	    y = str(x)
	    f.write(y + "\n")