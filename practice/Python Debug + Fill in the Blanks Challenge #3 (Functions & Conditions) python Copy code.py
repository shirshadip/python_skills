def check_even_or_odd_number(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

num = input("Enter a number: ")
check_even_or_odd_number(number=int(input("Enter a number: ")))
