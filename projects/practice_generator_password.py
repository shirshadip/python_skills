import string 
import random


def generator(legnth=16):
    char = string.ascii_uppercase + string.ascii_letters +string.punctuation
    password = ''.join(random.choice(char)for i in range(5))



print (generator)