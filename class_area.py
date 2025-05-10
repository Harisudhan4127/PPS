class rectangle_area:
    def dimention(self, lenght, width):
        area = lenght * width
        print(f'Area of the Rectangle is {area}.')

length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))

rect = rectangle_area()
rect.dimention(length, width)
