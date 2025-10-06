import numpy as np 
#1d array 
arr1 = np.array([1,2,3,4])

#2d array
arr2= np.array([[1,2,3],[5,6,7]])
print (arr1)
print (arr2)

#checking array properties

print (arr2.ndim)#number of dimensions 
print (arr2.shape)#rows and columns
print (arr2.size)
print (arr2.dtype)#data type of elements