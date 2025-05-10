# List
lib = ["books", "author", "barcodenumber","price"]
lib[0] = "ramayanam"
print(lib[0])
lib[1]= 'valmiki'
lib[2]= 101261
lib[3]= 234
print(lib)

# Tuple
t1 = (12134,250000)
t2 = ('book', 'totalprice') 
# t1[0] = 100 ----- Not assigned in tuple
# so let's create a new tuple as follows
t3 = t1 + t2
print(t3)