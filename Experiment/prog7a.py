def reverse(string):  
    string = string[::-1]  
    return string 

s = "ABDUR RASEEM AYYOUBI" 
print ("The original string is : ", s)  
 
print ("The reversed string(using extended slice syntax) is : ") 
print (reverse(s))
