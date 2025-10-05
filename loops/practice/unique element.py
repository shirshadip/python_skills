arr = [1,5,45,75,81,1,1,2,45,4]

unique_elements = []
for i in arr:
    if arr.count(i) == 1:
        unique_elements.append(i)

print("first Unique element:", unique_elements[0])