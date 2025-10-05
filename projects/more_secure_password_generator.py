import secrets
import string 

def password_generator (legnth=16):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(secrets.choice(characters)for i in range (legnth))
    return password 

print (password_generator)