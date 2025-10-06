#creating arrays quickly
'''numpy haas built-in functions to create arrays'''
import numpy as np
a = np.zeros((2,3)) #2x3 array of zeros 
b = np.ones((2,3))#2x3 array of ones 
c = np.arange(0,10,2)# 0 to 8 with step 2
d = np.linspace (0,1,5)#5 numbers between 0 and 1
e = np.eye(3)#3x3  identity matrix
print (a,"\n")
print (b,"\n")
print (c,"\n")
print (d,"\n")
print (e,"\n")