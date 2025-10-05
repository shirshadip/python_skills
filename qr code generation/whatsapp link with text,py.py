import qrcode
data = "https://wa.me/918910284853?text=Hello%20shirshadip"

qr = qrcode.make(data)
qr.save("whatsapp_link_with_a_msg.png")

print ("qr code generated succesfully")