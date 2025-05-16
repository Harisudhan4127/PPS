a = input("Enter a string : ") 
count = 0 
for c in a : 
    if c.isspace() != True: 
        count = count + 1 
print("Total number of characters : ",count) 
