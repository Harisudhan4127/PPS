#SETS

cars = {'BMW', 'Honda', 'Audi', 'Mercedes', 'Honda', 'Toyota', 'Ferrari', 'Tesla'} 
print('Approach 1 : ', cars) 
 
print('Approach 2 : ') 
for car in cars: 
    print("Car name = {}".format(car)) 

cars.add('Tata') 
print('New cars set = {}'.format(cars)) 
cars.discard('Mercedes') 
print('discard() method = {}'.format(cars))

#DICTIONARIES

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
# Adding elements one at a time 
Dict[0] = 'BRICKS' 
Dict[2] = 'CEMENT' 
Dict[3] = 'BLUE PRINT' 
print("Dictionary after adding 3 elements: ") 
print(Dict) 
# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4 
print("Dictionary after adding 3 elements: ") 
print(Dict) 
# Updating existing Key's Value 
Dict[2] = 'STEEL' 
print("Updated key value: ") 
print(Dict) 
# Adding Nested Key value to Dictionary 
 
 
Dict[5] = {'Nested': {'1': 'LIME', '2': 'SAND'}} 
print("Adding a Nested Key: ") 
print(Dict) 
