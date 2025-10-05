with open ("image.png","rb") as src:
    data = src.read()
with open ("copy.png","wb") as dst:
    dst.write (data)

print (data)