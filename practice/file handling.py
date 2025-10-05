# This code is supposed to write and read from a file

file = open("data.txt", "w")
file.write("Hello, this is a test file.")
file.close()

file = open("data.txt", "r")
content = file.read()
print("File content is:", content)
file.close()
