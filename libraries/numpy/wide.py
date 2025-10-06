import numpy as np
#These operations happen on the entire array:
matrix=np.array([[1,2,3],
                 [4,5,6]])
print (matrix.sum())#sum of all elements 
print (matrix.sum(axis=0)) #column wise sum
print (matrix.sum(axis=1))#row wise sum
print(matrix.mean())#average of all elements