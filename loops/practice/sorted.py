arr = [1,5,5452,4,2,6,5,8]
arr.sort()
is_sorted = True

for i in range (len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
    

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")
