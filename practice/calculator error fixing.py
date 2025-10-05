def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operation (add/sub/mul/div): ")

result = calculator(x, y, op)
print("Result is:", result)
