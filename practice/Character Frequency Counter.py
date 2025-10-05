def count_chars(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    return freq

user_input = input("Enter a string: ")
user_input = user_input.lower()  # Convert to lowercase
print(count_chars(user_input))
