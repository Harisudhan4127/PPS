# single inheritance

'''
class parent():
    def odd_even(self):
        num = int(input("Enter the Number : "))
        if (num%2 != 0):
            print(f"Odd is {num}.")
        else:
            print(f"Even is {num}.")

class child(parent):
    def add(self, a,b):
        print(f"A + B = {a+b}.")

c= child()
print("parent")
c.odd_even()  
print("child")  
c.add(a= int(input("Enter the Number A : ")),b= int(input("Enter the Number B : ")))
print("-----completed----") 

'''

# Multple inheritance   
'''
class father:
    def parent(self):
        print("parent class - Father")

class mother:
    def parent2(self):
            print("parent class - Mother")
    
class child(father, mother):
    def __init__(self):
        print("Child class - son")

c = child()
c.parent()
c.parent2()

'''

# Multple-level Inheritance

'''
class grandfather():
    def parent1(self):
        print("grandfather")

class father(grandfather):
    def parent2(self):
        print("Father")

class son(father):
    def children(self):
        print("children")

s = son()
s.children()
s.parent2()
s.parent1()

'''

# Hierarchical Inheritance

'''

class father:
    def parent(self):
        print("parent class - Father")

class mother:
    def parent2(self):
            print("parent class - Mother")

    
class child(father, mother):
    def child(self):
        print("Child class - son")
        
class son(child):
    def son(self):
        print("son")
        
s = son()
s.parent()
s.parent2()
s.child()
s.son()

'''

