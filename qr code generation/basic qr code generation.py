import qrcode
data = "hello,this is a basic qr code"

qr = qrcode.make(data)
qr.save("basic_qrcode.png")

print("qr code generated succesfully")
