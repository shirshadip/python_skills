li=[1,2,3,4,6,54,1,2,3]
sor= sorted(li)
for check in range (len(li)):
    ch=check+1
    if sor [check]==sor[ch]:
        print (sor)
    else :
        print ("no duplicates are there")