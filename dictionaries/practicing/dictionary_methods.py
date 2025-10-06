'''
Dictionary Methods

Create a dictionary of 3 subjects and marks.

Use .keys(), .values(), and .items() to display data.

Find the subject with the highest marks.
'''

result = {
    "maths":25,
    "physics":35,
    "bengali":55
}
print (result.keys())
print (result.get("maths"))#returns 25
print(result.values())
print(result.items())
print(max(result.values()))



