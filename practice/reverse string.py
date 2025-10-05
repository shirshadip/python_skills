def reverse_string(text):
    reversed = ""

    for i in range (len(text)-1, -1, -1):
        reversed = reversed +text[i]
    return reversed
user_input = input ("enter a string:")
print ("reversed string is: ",reverse_string(user_input))