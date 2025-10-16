# Create a user-defined integer list
li = list(map(int, input("Enter integers separated by space: ").split()))

# Ask the user for the element to find
element = int(input("Enter the element to find: "))

# Find all positions (to handle duplicates)
positions = [i for i, num in enumerate(li) if num == element]

if not positions:
    print("Element not found in the list.")
else:
    for pos in positions:
        print(f"\nElement {element} found at position {pos + 1}")
        
        # Handle edge cases for first and last element
        if pos == 0:
            print("It is the first number.")
            if len(li) > 1:
                print("Next element:", li[pos + 1])
        elif pos == len(li) - 1:
            print("It is the last number.")
            print("Previous element:",li[pos - 1])
        else:
            print("Previous element:", li[pos - 1])
            print("Next element:", li[pos + 1])

# Find and print duplicate numbers
duplicates = []
for num in set(li):
    if li.count(num) > 1:
        duplicates.append(num)

if duplicates:
    print("\nDuplicate numbers in the list:", duplicates)
else:
    print("\nNo duplicate numbers found.")
