import qrcode
#replace with your full number(country code + number),no '+'
data = "https://wa.me/918910284853"

#creating qr code
qr = qrcode.make (data)
qr.save("whatsapp_qrcode.png")

print ("qr code generated succesfully")




