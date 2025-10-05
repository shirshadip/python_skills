import random
choose = input ("choose level\n"
                "1. easy(1,10)\n"
                "medium(1,100)\n"
                "hard(1,1000):")
attempt = 1
while True:
    if choose == "1":
        number = random.randint(1,10)
        guess = int (input ("enter your guess: \n"
        f"write your guess\n"
           f"in {attempt} attempts\n"
           f""))
        if guess < number:
            print ("your guess is too low")
            attempt += 1
            print (f"attempt number.{attempt} ")
        elif guess > number:
            print ("your guess is too high")
            attempt += 1
            print (f"attempt number.{attempt} ")
        elif guess == number:
             print (f"congratulations you guessed the correct number in {attempt} attempts")
             break
        else:
            print ("Invalid input. Please enter a number.")
            break

    if choose == "2":
        number = random.randint(1,100)
        guess = int(input("enter your guess: \n"
                          f"write your guess\n"
                          f"in {attempt} attempts\n"
                          f""))
        if guess < number:
            print("your guess is too low")
            attempt += 1
            print(f"attempt number.{attempt} ")
        elif guess > number:
            print("your guess is too high")
            attempt += 1
            print(f"attempt number.{attempt} ")
        elif guess == number:
            print(f"congratulations you guessed the correct number in {attempt} attempts")
            break
        else:
            print("Invalid input. Please enter a number.")
            break

