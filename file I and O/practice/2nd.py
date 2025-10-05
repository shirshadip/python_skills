fname=input("enter the  file name where you want to append lines:")
with open(fname,"a") as a :
    line = input ("enter the content which you want to append :->")
    print (a.write(line))
   