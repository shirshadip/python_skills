n= int (input ("enter terms: "))
fno =0
sno = 1
print ("febonacci series up to ",n,"terms are:",fno,", ",sno,end=" ")
for i in range (2,n):
    tno = fno +sno
    print (", ",tno , end=" ")
    fno = sno 
    sno = tno 