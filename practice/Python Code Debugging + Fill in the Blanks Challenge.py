def greet_user(name):
    print("Hello" + name)
    if len(name) > 0:
         print("Your name has", len(name), "letters")
    else:
         print("You didn't enter any name.")
    
greet_user(name=str(input("Enter your name: ")))


