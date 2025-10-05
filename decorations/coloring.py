# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

''''
lets animate the display of execution of python scripts 

'''
import time 
import sys 
code = [
   RED+ "x = 5"+RESET,
   YELLOW+ "y= 10"+RESET,
    BLUE+"print ('result:',z)"+RESET,
    GREEN+"PROGRAM FINISHED"+RESET
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
