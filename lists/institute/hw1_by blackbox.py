

# Program to search for an element in a user-defined integer list
# and handle positions, previous/next elements, and duplicates
# Step 1: Get the list from the user
input_str = input("Enter integers separated by commas (e.g., 1,2,3,2,4): ")
# Split the input string and convert to a list of integers
my_list = [int(x.strip()) for x in input_str.split(',')]
# Step 2: Get the element to search for
try:
    search_element = int(input("Enter the element to search for: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
# Step 3: Search for the element in the list
positions = []  # To store 1-based positions of the element
for index, element in enumerate(my_list):  # enumerate uses 0-based index
    if element == search_element:
        positions.append(index + 1)  # Convert to 1-based position
if positions:  # If positions list is not empty, element is found
    print(f"Element {search_element} found at position(s): {positions}")
    
    for pos in positions:  # Process each position
        print(f"\nProcessing position {pos}:")
        
        # Check for previous element
        if pos > 1:
            prev_index = pos - 2  # 0-based index for previous element
            print(f"Previous element: {my_list[prev_index]}")
        else:
            print("It is the first number")
        
