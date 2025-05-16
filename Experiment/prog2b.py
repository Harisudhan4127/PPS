n = int(input("Enter number of values : ")) 
l = [] 
for val in range(0,n,1): 
      e = int(input("Enter integer : ")) 
      l.append(e) 
print("Circulating the elements of list ", l) 
for val in range(0,n,1): 
       e = l.pop(0)
       l.append(e)
       print(l) 
