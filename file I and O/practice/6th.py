try:
    file = open ("newfile.txt","r")
    content = file.read()
    print (content)
finally:
    file.close()