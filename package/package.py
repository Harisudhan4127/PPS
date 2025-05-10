def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c= a-b
    return c
def mult(a,b):
    c = a*b
    return c
def div(a,b):
    c=a/b
    return c
def selection(opition, a, b):
    if opition == 1 :
        print(f'Add of a and b is {add(a,b)}')            
    elif opition ==2:
        print(f'Sub of a and b is {sub(a,b)}')    
    elif opition ==3:
        print(f'Mult of a and b is {mult(a,b)}')    
    elif opition ==4:
        print(f'Div of a and b is {div(a,b)}')
    else:
        print("Your Enter Opition is incorrecr of ERRO")
        