import math
counter = 1
value = int(input("enter value:"))
while(value > 3):
    counter += 1
    value = math.ceil(value / 3)

print(counter)