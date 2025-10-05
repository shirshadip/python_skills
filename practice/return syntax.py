#running a value 
def addition(a,b):
    return a + b 
result = addition(int (input ("enter a num:")), int (input ("enter another num:")))
print("the sum is:",result)

#ending a function early 
def check_number (x):
    if x < 0:
        return "negative"
    return "positive"
    if x == 0:
        return "zero"
    return "invalid input"

print (check_number(int(input("enter a number:"))))


#returning multiple values 
def calculate (a,b):
    return a + b, a - b, a * b, a / b

result = calculate(int(input("enter a num:")), int(input("enter another num:")))
print("the results are:", result)