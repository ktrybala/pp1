import random
roll_amount = int(input("How many times you want to roll the dice: "))

#wartosci zmiennych
y = 1
sum = 0

#rzut kostka
while y <= roll_amount:  
   x = random.randint(1,6)
   sum += x
   y += 1

print(sum)