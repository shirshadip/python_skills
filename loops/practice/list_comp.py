#list of squares 
squares = [x**2 for x in range (10)]
print (squares)

#generator expressions 
squares_gen= (x**2 for x in range (10))
for s in squares_gen:
    print (s,end=" ")