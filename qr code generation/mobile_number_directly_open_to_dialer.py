import qrcode   
data = "tel:8910284853"

qr = qrcode.make(data)
qr.save("mobile_number_link.png")

print ("qr code generated succesfully")

