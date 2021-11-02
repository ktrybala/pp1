from random import *

def rand(x,y):
	z = 0
	
	while z != 1:
		number = randint(x,y)
		if number % 3 == 0 and number % 2 == 0:
			print(number)
			z += 1


		

