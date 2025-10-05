import random 

print ("prints a random floating number between 0 and 1: ", random.random())
print ("prints a random integer",random.randint(2,40))
print ("random float between 4 to 10",random.uniform(4,10))
print ("random choice from a list", random.choice(['apple', 'banana', 'cherry']))
print ("random sample of 3 elements from a list", random.sample(['apple', 'banana', 'cherry', 'date', 'fig'], 3))

fruits = ["mango", "banana", "apple","pineapple"]
random.shuffle(fruits)
print ("prints a shuffled list of fruits: ", fruits)