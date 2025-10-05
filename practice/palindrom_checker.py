def is_palindrome(text):
    #remove spaces and make lowercase for comparison
    cleaned= text.replace(" ","").lower()
    return cleaned == cleaned [::-1]

#example usage 
word = input ("enter a word or phrase:")
if is_palindrome(word):
    print ("is a palindrome")

else: 
    print("is not a palindrome")

