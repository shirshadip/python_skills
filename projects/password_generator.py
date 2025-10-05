import random
import string 

def password_generator(legnth=12):
    #characters to use : letters, digits, and symbols
    characters = string.ascii_letters + string.digits +string.punctuation
    password =''.join(random.choice (characters)for i in range (legnth))
    return password

print ("generated password is:",password_generator)