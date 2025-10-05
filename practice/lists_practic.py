#creating list
fruits = ["mangos", "bananas", "apples", "cherry", "grapes"]
print(fruits)
print(type(fruits))

print(fruits[0]) #prints the first item ##mangos 
print(fruits[1]) #prints the second item ##bananas
print(fruits[-1])#printsw last item ##"apples"

print (fruits[1:4])#prints second to 4th
print (fruits[:3])#prints first 3
print(fruits[2:])#prints last 3
print(fruits[-3:])#prints the last 3rdth

fruits[3]="orange"
print(fruits)


#modify multiple items using slicing 

numbers = [1,2,3,4,5]

numbers[1:3]=[20,30]

print(numbers)#[1,20,30,4,5]

fruits.append("pineapple")
print(fruits)
fruits.insert(1,"royalfruit")
print(fruits)#inserts at a specefic position

#adds multiple items
fruits.extend(["guava","pear"])
print(fruits)

fruits.remove("royalfruit")
print(fruits)
