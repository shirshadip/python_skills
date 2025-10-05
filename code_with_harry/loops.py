l= [1,3,4,5,6,7]

for i in l:
    print (i)

else:
    print("No more elements in the list")



for i in range(100):
    if (i==23):
        print ("Found 23")
        break
    print(i)

for i in range(100):
    for j in range(100):
        if (j == 45):
            print("Found 45")
            continue
        print(j)