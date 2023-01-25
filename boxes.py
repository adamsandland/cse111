import math

items = int(input("Please Enter the number of Manufactured Items: "))
packCount = int(input("How many of these items fit in a box? "))
solution = math.trunc(items/packCount)
if items%packCount>0:
    solution = solution+1
print(f"The number of boxes needed is {solution}")