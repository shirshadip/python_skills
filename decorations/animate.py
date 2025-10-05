''''
lets animate the display of execution of python scripts 

'''
import time 
import sys 
code = [
    "x = 5",
    "y= 10",
    "z = x +y"
    "print ('result:',z)"
]
for line in code:
    #simulate typing the code 
    for char in line :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) #typing speed 
    print () #move to the next line 
    time.sleep(0.5) #wait before showing result 


    #execute the line if it contains a print or assignment 
    try:
        exec(line)
    except:
        pass