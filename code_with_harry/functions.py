'''def avg():
    a = int (input ("enter a number:"))
    b = int (input ("enter a number:"))
    c = int (input ("enter a number:"))
    d = int (input ("enter a number:"))
    e = int (input ("enter a number:"))
    print ("Average is:", (a+b+c+d+e)/5)
avg()
print ("Done")'''

from math import factorial


def greet(name,ending="thanks"):
    print ("hello", name)

greet("Alice", "thanks")
greet("Bob")

fact=factorial(4)
print(fact)