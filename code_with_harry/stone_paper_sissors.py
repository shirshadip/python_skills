import random 

choice = random.choice(['stone', 'paper', 'scissors'])
user = input("Enter your choice (stone, paper, scissors as 1. 2. 3.): ")
def s_p_t():
    if user == choice:
        print ("It's a tie!")

    elif user == "1":
        if choice == "paper":
            print ("you loose")
            print ("computer choosed paper!")

        elif choice == "scissors":
            print ("you win")
            print ("computer choosed scissors!")
    elif user =="2":
        if choice == "stone":
            print ("you win")
            print ("computer choosed stone")

        elif choice == "scissors":
            print ("you loose")
            print ("computer choosed scissors!")

    elif user =="3":
        if choice =="stone":
            print ("you loose")
            print ("computer choosed stone!")
        elif choice == "paper":
            print ("you win")
            print ("computer choosed paper!")
    else:
        print ("Invalid input")

s_p_t()