'''import math
n = int (input ("enter a number:"))
print (math.factorial(n))'''

n = int (input ("enter a number you want to find factorial:"))
fact = 1

for i in range (1, n +1 ):
    fact = fact * i
print ("the factorial of the number is : ", fact)

#using while loop 

n = int(input("Enter a number: "))

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("Factorial:", fact)
# this code is to find the factorial of a number