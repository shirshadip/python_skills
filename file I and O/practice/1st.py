with open (input("enter the file name which you want to make or write  :"),"w") as w:
    content = input("write the content here:\n")
    w.write(content)

filename = input("enter the file name  which you want to read:")
with open(filename, "r") as r:
    print(r.read())