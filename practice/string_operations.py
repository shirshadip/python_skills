s = "hello, world!"
#length of a string 
print (len(s))
#accessing characters 
print (s[0]) #for first character
print (s[-1]) #for last character

#slicing a string 
print(s[7:]) #slicing from the 7th character to the end#output is world!
print(s[:5]) #slicing from the start to the 5th character#output is hello

#concatenation of string 
s2 = "hi,shirshadip,"
print (s2 + "how are you?") #output is hi,shirshadip,how are you?
#repetition of string
s3 = "hi, shirshadip! "
print(s3 * 2) #output is hi, shirshadip! hi, shirshadip!
# repetition of string with a space
print((s3 + " ") * 2)  # output: hi, shirshadip! hi, shirshadip!
#output: hello, world! hello, world!
print((s + " ") * 2)  # output: hello, world! hello, world!

#case conversion 

print(s.upper())  # output: HELLO, WORLD!
print(s.lower())  # output: hello, world!
print(s.title())  # output: Hello, World!

#whitespace stripping 
s4 = "     hello,      world   "
print (s4.strip ())  # output: hello, world
print (s4.lstrip ()) # output: hello,      world
print (s4.rstrip ()) # output:      hello,      world

#replacing substrings 

print (s.replace("world","shirshadip"))  # output: hello, shirshadip!

#spliting strings

print (s.split()) # output: ['hello,', 'world!']
print (s.split(",")) # output: ['hello', ' world!']

#joining strings 

word =["hello","world"]
print ("".join(word))  # output: helloworld
print ("-".join(word))  # output: hello-world

#checking for substring presence 
print ("world" in s) # output: True
print ("shirshadip" in s) # output: False

#checking for substring absence
print ("shirshadip" not in s) # output: True
print ("world" not in s) # output: False

#startswith and endswith 
print (s.startswith("hello"))  # output: True
print (s.endswith("world!"))  # output: True
print (s.startswith("world"))  # output: False
print (s.endswith("hello"))  # output: False

