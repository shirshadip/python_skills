fruits = ["apple", "banana", "cherry"]

#append (add at end)
fruits.append("orange")
print (fruits)

#insert (add at a specefic position)
fruits.insert(1,"grapes")

print (fruits)
#extend (add multiple elements)
fruits.extend(["kiwi","mango"])
print (fruits)

# ...existing code...
# Add multiple elements at a specific position (e.g., index 2)
fruits[2:2] = ["pear", "plum"]
print(fruits)
# ...existing code...