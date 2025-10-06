#slicing(getting a range of elements )
import numpy as np
arr= np.array([10,20,30,40,50])
print (arr[1:4])    #elements from index 1 to 3
print (arr[:3])     #first 3 elements
print (arr[2:])     #from index 2 to end 
print (arr[::2])    #every 2nd element 