def ispalindrome(s):
    return s == s[::-1] # Reverse that word is equal to given word

s = input("Enter the string = ")
flag = ispalindrome(s)

if flag :
    print("The string is palindrome")
    
else:
    print("The string is not a palindrome")
    