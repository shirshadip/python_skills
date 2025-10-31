
def kri (n):
    temp = n
    sum_fact = 0

    while temp > 0:
        digit = temp % 10

        # find factorial of each digit
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        # add to sum_fact
        sum_fact += fact
        temp //= 10

    # check condition
    if sum_fact == n:
        print(f"{n} is a Krishnamurti number.")
    else:
        print(f"{n} is not a Krishnamurti number.")
a = int(input("Enter a number: "))
kri(a)
