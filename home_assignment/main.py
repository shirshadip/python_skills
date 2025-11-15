# main.py

import palindrome as p

string = input("Enter a string: ")

if p.check(string):
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
