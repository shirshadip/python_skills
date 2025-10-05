'''use a context manager (with statement):'''

with open ("example.txt","r") as file:
    data= file.read()
    print (data)
# file is automatically closed 