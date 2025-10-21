#write a python program to find out all prime numbers between a range 
start= int (input ("enter the number where you wants to start:"))
end = int (input ("enter the number where you wants to end:"))


for i in range (start,end+1):
    if i==1 or i==0:
        print (i,"is neither prime nor composite")
    elif i>2:
        for j in range (2,i):

            if i%1==0 and i%j==0:
                print (f"{i} is composite number")
                break
            else :
                print (f"{i} is a prime number")
                break        
    else:
        print (f"{i} is a prime number")
 