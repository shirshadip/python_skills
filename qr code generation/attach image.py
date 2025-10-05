import qrcode

data = "https://media.tenor.com/rYTKte0-G1oAAAAM/alakh-pandey-physics-wallah.gif"

qr = qrcode.make (data)

qr.save("important_info.png")

print ("qr code generated succesfully")
