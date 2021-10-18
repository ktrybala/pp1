import random

roll = random.randint(1,6)

guess = int(input("Try to guess the dice roll number: "))

if (guess == roll):
	print("Good job, you guessed the number! ")
else:
	print("Wrong number, try again. ")