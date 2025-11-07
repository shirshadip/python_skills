srange = int (input ("enter the starting number:"))
erange = int (input ("enter the ending number:"))
for x in range (srange,erange+1):

    # num = 145
    temp = x
    sum_factorial = 0

    while temp > 0:
        digit = temp % 10
        print("Digit:", digit)

        fact = 1  # ✅ Reset factorial for each digit
        for f in range(1, digit + 1):
            fact *= f
        
        print("Factorial of", digit, "=", fact)
        
        sum_factorial += fact  # ✅ Add after full factorial is calculated
        temp //= 10

    print("Sum of factorial digits =", sum_factorial)

    if sum_factorial == x:
        print(x, "is a Krishnamurthy Number ✅")
    else:
        print(x, "is not a Krishnamurthy Number ❌")
