import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[:2,1:]) #top 2 rows and last 2 columns 
print (matrix[1:,:2]) #last 2 rows , first 2 columns