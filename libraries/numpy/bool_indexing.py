#boolean indexing (super useful!)
#you can filter values based on conditions 

import numpy as np
arr= np.array([10,20,30,40,50])

print (arr[arr>25]) #elements greater than 25 
print (arr[arr%20==0]) #elements divisible by 20