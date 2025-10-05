import qrcode  


#upi payment info 
upi_id = "yourupiid@bank" #your upi id 
name = "shirshadip" #your name
amount = "1" #optional
currency = "INR"

#upi link 
upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

#generate qr
qr = qrcode.make(upi_link)
qr.save("upi_qr.png")

print ("upi qr code generated succesfully")



#####################if you dont want to fix the payment amount 
import qrcode

# UPI payment info
upi_id = "yourupiid@bank"   # Replace with your UPI ID
name = "Shirshadip"         # Replace with your name
currency = "INR"

# UPI link without amount
upi_link = f"upi://pay?pa={upi_id}&pn={name}&cu={currency}"

# Generate QR
qr = qrcode.make(upi_link)
qr.save("upi_no_amount_qr.png")

print("✅ UPI QR code (no amount) saved as 'upi_no_amount_qr.png'")
