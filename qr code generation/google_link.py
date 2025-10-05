import qrcode  
data = "www.google.com"
qr = qrcode.make(data)
qr.save("google_link.png")

print ("qrcode generated succesfully")