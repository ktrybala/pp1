import math 
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))
sqr_height = (height/100)**2
bmi = (weight)/sqr_height
#wynik bmi zostanie zaokragony do setnych
print(f"Your BMI is: {round(bmi,2)} ")