
n = int (input ("enter the number of range you want to stop your loop :"))
rev = 0 
temp = n 

while (temp > 0):
    digit = temp %10

    rev = rev * 10 +digit 
    temp //= 10 

print ("the reverse of the number is : ", rev)
