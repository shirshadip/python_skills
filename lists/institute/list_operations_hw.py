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
        print ("The previous element is -->",li[prev])
        '''print ("The next element is -->",li[next])'''
        if index==0:
            print ("this is the first element of the list")
        
        elif index == revli[0]:
            print ("this is the last element of the list")