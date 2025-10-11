st = int (input ("enter a number:"))
en = int (input ("enter another number:"))
pc = 0
cc =0
for num in range (st,en+1):
    f = 0
    mg = " "
    for i in range (2,num):
        if num %i==0:
            
        if f ==0:
            print (num,"is a prime number because its only divisable by 1 &",num)
            pc =pc +1
