import random as r 
def shuf (name ):
    l_name = name.split()
    ret= ""
    for i in range (len(l_name)):
        s_name = r.choice(l_name)
        ret+= s_name + " "
    return ret
n= input("enter a name:")
print(shuf (n))