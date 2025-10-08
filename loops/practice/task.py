# Program to print all prime and composite numbers in a given range
print ("="*15,"prime or composite number checking","="*15)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
prime =0
compos=0

for num in range(start, end + 1):
    if num > 1:  # Only numbers greater than 1 can be prime or composite
        factors = []
        for i in range(2, num):
            if num % i == 0:
                factors.append(i)
        if factors:
            compos += 1
            print(f"{num} is a Composite number because the factors of {num} are --> {factors} and {1} and {num}")
        else:
            print(f"{num} is a Prime number because {num} is divisible by only 1 and {num} itself")
            prime += 1
    else:
        print(f"{num} is neither Prime nor Composite")

print (f"there are {prime} prime numbers between {start} to {end}")
print (f"there are {compos} composite numbers between {start} to {end}")