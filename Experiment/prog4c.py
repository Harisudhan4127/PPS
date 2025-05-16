#LIST
m= ["cementbags", "bricks", "sand", "steelbars", "paint"]  
m.append('Tiles') 
m.insert(3,'Aggregates') 
m.remove('sand') 
m[5]='electrical' 
print(m)  

#TUPLE: 
m = ("cementbags", "bricks", "sand", "Steelbars", "Paint")  
print(m) 
print ("list of element is : ",m)  
print ("materials[0]: ", m [0])  
print ("materials[1:3]: ", m [1:3])
