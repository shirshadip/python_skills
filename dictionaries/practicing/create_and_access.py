'''
Create & Access

Create a dictionary of 5 countries and their capitals.

Print the capital of India.

Add a new country-capital pair.

Delete one country.'''

country= {
    "India":"delhi",
    "UAE":"Abu dabhi",
    "China":"Beijing",
    "Thiland":"Bankok",
    "Nepal":"Kathmandu"
}
print(country["India"])

country["Bangladesh"]="Dhaka"
print (country)
del country["UAE"]
print (country)
