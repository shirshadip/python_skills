rows = int(input("enter the number of rows you want:"))
for i in range (1,rows +1 ):
    for j in range (1,i+1):
        print (j,end = "")
    print ()

rows = int(input("enter the number of rows you want:"))
for i in range (1,rows+1):
    print (" "*(rows - i ),end = " ")
    for j in range (1,i+1):
        print (j,end =" ")
    print()

rows = int(input("enter the number of rows you want:"))
for i in range (rows , 0,-1):
    for j in range (1,i+1):
        print (j,end = " ")
    print ()

rows = int(input("enter the number of rows you want:"))
for i in range (1,rows +1):
    print (" "*(rows -i)* 2,end = "")#add space for all alignments
    for j in range (1,i+1):
        print (j,end = " ")
    print ()


rows = int(input("enter the number of rows you want:"))
for i in range (1,rows +1):
    for j in range (i):
        print (i,end = " ")
    print()
# Heart shape using number pattern
rows = 6
for i in range(rows):
    for j in range(2 * rows + 1):
        if (i == 0 and (j == 1 or j == 5 or j == 7 or j == 11)) or \
           (i == 1 and (j == 0 or j == 2 or j == 4 or j == 6 or j == 8 or j == 10 or j == 12)) or \
           (i == 2 and j % 2 == 0) or \
           (i == 3 and (j >= 1 and j <= 11)) or \
           (i == 4 and (j >= 2 and j <= 10)) or \
           (i == 5 and (j >= 4 and j <= 8)):
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()
