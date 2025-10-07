# Matrix Operations using NumPy
# -----------------------------------------


import numpy as np

#create two 2x2 matrices
a= np.array([[1,2],
            [3,4]])

b = np.array([[5,6],
             [7,8]])

print ("matrix a:\n",a)
print("martrix b:\n",b)

print ("_"*30)

#matrix addition 
print ("a+b=\n",a+b)

#matrix subtraction
print ("a-b=\n",a-b)

#matrix multiplication (element wise )

print ("a*b=\n",a*b)

#matrix division (element wise )

print ("a/b=\n",a/b)

#matrix dot product (proper matrix multiplication)
print ("a dot b =\n",np.dot(a,b))
'''alternative method '''

print ("a @ b=\n",a @ b ) 

#transpose of matrix 
print ("transpose =\n",a.T)

#determinant
print ("determinant of matrix a =\n",np.linalg.det(a))

#inverse of a matrix

print ("inverse od a =\n",np.linalg.inv(a))

#rank  of a matrix 
print ("rank of a =\n",np.linalg.matrix_rank(a))



#  Eigenvalues and Eigenvectors

eigenvalues,eigenvectors=np.linalg.eig(a)
print ("eigenvalues:=\n",eigenvalues)
print ("eigenvectors:=\n",eigenvectors)