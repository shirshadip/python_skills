'''Create a dictionary of 5 fruits and their prices.

Use a loop to print each fruit with its price.

Increase all prices by 10%.
'''

fruits={
    "apple":20,
    "banana":45,
    "mango":22,
    "orange":35,
    "grapes":55
}
print("fruits and price->\n")
for fruit,price in fruits.items():
    print (f"{fruit}:{price}")

print ("\nafter 10% price increase\n")

for fruit in fruits:
    fruits[fruit]=round (fruits[fruit]*1.10)

for fruit , price in fruits.items():
    print (f"{fruit}:{price}")