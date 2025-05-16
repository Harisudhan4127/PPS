import math
x1 = int(input("enter the value of x1 = "))
x2 = int(input("enter the value of x2 = "))
y1 = int(input("enter the value of y1 = "))
y2 = int(input("enter the value of y2 = "))

dx = x2 - x1
dy = y2 - y1
d = dx**2 + dy**2
result = math.sqrt(d)
print(result)