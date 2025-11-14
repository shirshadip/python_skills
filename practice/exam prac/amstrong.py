#amstrong number
st = int (input ("enter the starting number :"))
en = int (input ("enter thr ending number :"))
for n in range (st,en+1):
    b = n#153
    c = 0#0+1
    while b > 0 :#3>0
        c +=1 
        b = b//10 #153//10
    bb = n #153
    arm = 0#0
    while bb >0 :
        m = bb % 10 
        arm =arm +m**c 
        bb //=10
    if n == arm:
        print (n, "is a amstrong number")
    else:
        print(n,"is not a amstrong number")