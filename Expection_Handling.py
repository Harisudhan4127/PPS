# a = int(input("Input a : "))
# b = int(input("Input b : "))
# try :
#     r =a/b 
#     print("10 / Input :", r) 
# except ZeroDivisionError :
#     print("Input is Error" , ZeroDivisionError)
    
# else:
#     print("No Problem")
    
try :
    age = int(input("Enter the Age : "))
    if age >= 18:
       print("Your are age able voting") 
    else:
        print("Your are Not able voting")
        
except ValueError:
    print(ValueError)
            