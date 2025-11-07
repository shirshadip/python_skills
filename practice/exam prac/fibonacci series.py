def fibo (n):
    if n <= 1:
        return n
    else :
        return fibo (n-1)+fibo (n-2)
t = int (input("terms are :"))
# fibo(t)
print ("fibonacci series are ---->")

for i in range (1,t+1):
    print(fibo(i),end=" ")

