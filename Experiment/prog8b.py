import numpy as np 
a = np.arange(6) 
a2 = a[np.newaxis, :] 
a2.shape 
#Array Creation and functions: 
a = np.array([1, 2, 3, 4, 5, 6]) 
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) 
print(a[0]) 
print(a[1]) 
np.zeros(2) 
np.ones(2) 
np.arange(4) 
np.arange(2, 9, 2) 
np.linspace(0, 10, num=5) 
x = np.ones(2, dtype=np.int64) 
print(x) 
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8]) 
np.sort(arr) 
a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8]) 
np.concatenate((a, b)) 
#Array Dimensions: 
array_example = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0 ,1 ,2, 3], [4, 5, 6, 7]]]) 
array_example.ndim 
array_example.size 
array_example.shape 
a = np.arange(6) 
print(a) 
b=a.reshape(3, 2); print(b) 
