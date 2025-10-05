
my_info = {
    "name":"shirshadip",
    "age":16,
    "school":"knv"
}

#loop through keys
for key in my_info:
    print (key)

#loop through values
for value in my_info.values():
    print ("\n",value)

#loop through key value pairs
for key,value in my_info.items():
    print (key," : " , value )


sub ={
    "1st sub": "maths",
    "2nd sub": "physics",
    "3rd sub": "computer science",
}
for keys, value  in sub.items():
    print (keys, " : ", value)