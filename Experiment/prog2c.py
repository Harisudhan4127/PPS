import math
x1 = int(input("Enter the value of x1 : "))
x2 = int(input("Enter the value of x2 : "))
y1 = int(input("Enter the value of y1 : "))
y2 = int(input("Enter the value of y2 : "))

d1 = x2-x1
d2 = y2-y1

d = d1**2 + d2**2
result = math.sqrt(d)
print(result)
