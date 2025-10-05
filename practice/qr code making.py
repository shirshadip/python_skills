import qrcode

data = "shirshadip"
qr = qrcode.make(data)

qr.save("myname.png")

print ("qr code generated succesfully")