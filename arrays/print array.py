arr = [10,20,50,60,40]

print ("Array:",arr)

print ("first elememt:",arr[0])
print ("last",arr[4])
print ("last",arr[-1])

#insert elements 

arr.append(70) #add at the end 
arr.insert (2, 45) #add at the 2nd index

print ("after inserting :",arr)

#delete elements 

arr.remove(70) #remove by value 
del arr[2] #remove by the index number

print ("after deleting :",arr)

#updating elements 

arr[0] = 100
print ("after updating:",arr)

arr.sort () #ascending 
arr.sort(reverse=True) #descending order
arr.reverse() #reverse current order
print ("sorted array:",arr)

#find maximum , minimum , sum 

print ("max", max(arr))
print ("min",min(arr))
print ("sum:",sum(arr))
