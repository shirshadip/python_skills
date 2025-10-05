import qrcode  

#mobile number shown as plain text 

data = "8910284853"

qr = qrcode.make(data)
qr.save("mobile_number.png")

print ("qrcode generated succesfully")
