import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperatures = re.findall("\d{2}",message)

x = (int(temperatures[0]) + int(temperatures[1]) + int(temperatures[2])) / len(temperatures)
print(int(x))