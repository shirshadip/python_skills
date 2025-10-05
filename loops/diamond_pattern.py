n = int (input ("enter the number of rows:")) #number of the rows for the diamond pattern
#top half
for i  in range(n):
    print (" "*(n-i-1)+"*"*(2*i+1))

#bottom half
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))