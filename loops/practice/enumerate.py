a = ["apple","banana","mango"]

for index, fruits in enumerate(a):
    print (index,fruits)

for index, fruit in enumerate(a, start=1):
    print(index, fruit)
b=list(enumerate(fruits))
print(b)

