# import os 
# file_path = os.path.join(r'C:\Users\AI&ML\Desktop\Python\text.txt')
# print(file_path)

# if os.path.exists(file_path) : 
#     with open (file_path, 'r') as file:
#         content = file.read()
#         print(content)
# else :
#     print('Your file is Not Founded')

import os 

path = os.path.join(r"D:\Git file\pps\Experiment\text.txt")

# print(path)
# os.remove(path)

with open(path,'r+') as file:
    text = file.read()
    print(text)