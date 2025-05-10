def cal_area (name):
    name = name.lower()
    if name == 'rectangle':
        l = int(input("Enter rectangle's Length: "))
        b = int(input("Enter rectangle's Breadth: "))
        area = l*b
        print(f"The area of rectangle is {area}.")
        
    elif name == 'square':
        a =  int(input("Enter Square's Side length: "))
        area = a*a
        print(f"The area of Square is {area}.")
        
    elif name == 'triangle':
        h = int(input("Enter Triangle's Height length: "))
        b = int(input("Enter Triangle's Breadth: "))
        area = 0.5*b*h
        print(f"The area of Triangle is {area}.")
        
    elif name == 'circle':
        r =  int(input("Enter circle's radius lenght: "))
        pi = 3.14
        area = pi*r**2
        print(f"The area of Circle is {area}.")
        
    elif name == 'parallelogram':
        h = int(input("Enter parallelogram's height length: "))
        b = int(input("Enter parallelogram's base length: "))
        area = b*h
        print(f"The area of parallelogram is {area}.")
        
    else:
        print('Sorry! This shape is not available')
        
if __name__ == "__main__" :
    print("Calculate Shape Area:")
    
shape_name = input("Enter the name of shape whose area you want to find : ")
cal_area(shape_name)