def cal_area(name):
    name = name.lower()
    if name == "rectangle":
        l = int(input("Enter rectangle's length : "))
        b = int(input("Enter rectangle's breadth : "))
        rect_area = l * b
        print(f"The area of rectangle : {rect_area}.")
    elif name == "square":
        s = int(input("Enter square's side length : "))
        sqt_area = s * s
        print(f"The area of square : {sqt_area}.")
    elif name == "triangle":
        h = int(input("Enter triangle's height length : "))
        b = int(input("Enter triangle's breadth length : "))
        tri_area = 0.5 * b * h
        print(f"The area of triangle : {tri_area}.")
    elif name == "circle":
        r = int(input("Enter circle's radius length : "))
        pi = 3.14
        circ_area = pi * r * r
        print(f"The area of triangle : {circ_area}.")
    elif name == 'parallelogram':
        b = int(input("Enter parallelogram's base length : "))
        h = int(input("Enter parallelogram's height length : "))
        para_area = b * h
        print(f"The area of parallelogram : {para_area}.")
    else:
        print("Sorry! This shape is not available")
print("Calculate Shape Area")
name1 = input("Enter the name of shape whose area you want to find : ")
cal_area(name1)
