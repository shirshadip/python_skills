with open ("notes.txt","w") as create:
    create.write("this file is created by python script\n")
    create.write("file handling is easy")

with open ("notes.txt","r") as read:
    print (read.read())