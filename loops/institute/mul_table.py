n = int (input("enter a number:"))
r = int (input ("enter another number to decide the range:"))
num = [x for x in range (1,11)]
for i in range (n,r+1):
    for j in range (len(num)):
        print (f"{i}x{num[j]}",i*num[j])