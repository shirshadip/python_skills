#number of lists element 
n = int (input ("enter how many elements you want?-->"))
li=[]
#inputting and creating list
for i in range (n):
    ele=int(input(f"enter the element of index no.{i}--->"))
    li.append(ele)
print (li)
revli=list(reversed(li))
#element searching 
choose =int (input ("enter which elements index no. you want to know?-->"))
for index in range (len (li)):
    
    #outputs 
    if li [index]==choose:
        print ("The index number of you searched element is -->",index)
        prev = index-1
        next=index+1
        if li[index]==li[0]:
            print ("this is the first element in the list")
            print ("the next element is -->",li[next])

        elif li[index]>li[0] and li[index] <li[-1]:
            print ("the previous element is -->",li[prev])
            print ("the next element is-->",li[next])
        elif li[index] ==li[-1]:
            print ("this is the last element of the list")
            print ("the previous element is",li[prev])
        else :
            print ("sorry!the element you searched ,not found in the list ")
#duplicate checking 
duplicates = []
for num in set(li):
    if li.count(num) > 1:
        duplicates.append(num)

if duplicates:
    print("\nDuplicate numbers in the list:", duplicates)
else:
    print("\nNo duplicate numbers found.")