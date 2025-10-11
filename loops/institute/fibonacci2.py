#fibonacci series with recursion
def fib (n):
    if n <=1:
        return 1
    else :
        return fib(n-1)+fib(n-2)
    
term=int (input ("enter the terms :"))
for i in range(term):
    print(fib(i),end=" ")