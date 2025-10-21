n=int(input("enter how many elements you want?-->"))
li=[]
for i in  range (n):
    ele=int(input(f"enter the element of index no.{i}--->"))
    li.append(ele)
print (li)    
choose = int (input ("which element do you want to find?-->"))
for index in range (len(li)):
    if  li[index]==choose:
        print ("element found at->",index)
    prev=index-1
    next=index+1
    if index==0:
        print ("this is the first element of the list ")
        print ("the next element of the list is -->",li[next])
    elif index>0 and index<0:
        print("the next element is -->",li[next])
        print ("the previous element is -->",li[prev])
    elif index==len(li)-1:
        print ("this is the last element of the list")
        print ("the previous element of the list is-->",li[prev])
#duplicates checking 
    