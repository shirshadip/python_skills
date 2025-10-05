arr = [1,1,2,5,4,5,4,58,5,5,4,5,5,5,5,4,7,9,93,4,4,7]
even=0
odd=0
for i in arr:
    if i % 2 == 0:
        print (i, "is even")
        even += 1
    else:
        print (i, "is odd")
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)