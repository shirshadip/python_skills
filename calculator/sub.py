def sub():
    total = float(input("Enter a number: ----> "))

    while True:
        b = input("Enter another number (or type 's' to stop): ----> ")

        if b.lower() == "s":
            break  # exit the loop
        else:
            total -= float(b)  # keep adding numbers

    return total
print("result",sub())