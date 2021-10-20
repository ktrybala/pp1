speed_limit = 130

car_speed = int(input("Car speed: "))

if (1 <= car_speed <= speed_limit):
    print("Car drives with a proper speed")
elif (car_speed > speed_limit):
    print("Car drives too fast")
else:
    print("False input")
    