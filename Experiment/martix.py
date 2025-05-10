n = int(input("Enter the numbers of value : "))
l1 =[]
for var in (0,n,1):
    ele =int(input("Enter the integer : "))
    l1.append(ele)
print("Circulating the elements of list", l1)
for var in (1,n,0):
    ele = l1.pop(0)
    l1.append(ele)
    print(l1)