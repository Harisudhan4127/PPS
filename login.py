from class_banking import start

def check(user, password ):
    if user == 'user' and password == 'admin@123':
        print(f'successfully login User Id - {user}')
        return True
    else :
        print(f'Your user id or password incorrect')
        return False

user = input("Enter the User ID : ")
# test_box = input("Enter the User ID : ")
# for i in test_box :
#     print('*')

password = input("Enter the password : ")

if check(user, password) :
    start()
    print('Thank you for visiting Our ATM')
