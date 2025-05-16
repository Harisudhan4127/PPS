n = int(input("enter the number "))
def pypart(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("*",end='')
        print("\r")
pypart(n)