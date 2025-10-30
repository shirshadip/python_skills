import random as r

def shuf(name):
    l_name = name.split()        # split name into list
    r.shuffle(l_name)            # shuffle the list in place
    ret = " ".join(l_name)       # join list back into a string
    return ret

n = input("Enter a name: ")
print(shuf(n))
