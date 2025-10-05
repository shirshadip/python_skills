a = input ("enter something:")
b = input ("enter something else:")

if a == "hello":
    print("Hello to you too!")
if b == "hi":
    print("Hi there!")

if b == " " and a != "":
    print("You entered a space for the second input.")
else:
    print ("empty input ")