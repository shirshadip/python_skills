# a converter for international currency exchange 
usd_to_gbp = 0.66
usd_to_eur = 0.77
usd_to_jpy = 99.18
usd_to_inr = 59.52

gbp_sign = '\u00A3'#unicode values for none-ASCII currency symbols
eur_sign = '\u20AC'
jpy_sign = '\u00A5'
inr_sign = '\u20B9'

dollars = 1000 #the number of dollars to convert

pounds = dollars * usd_to_gbp #conversion calculations
euros = dollars * usd_to_eur
yen = dollars * usd_to_jpy
rupees = dollars * usd_to_inr

print ("today , $" + str(dollars)) #prints the value of dollars
print ("converts to, " + gbp_sign + str(pounds))
print ("converts to, " + eur_sign + str(euros))
print ("converts to, " + jpy_sign + str(yen))
print ("converts to, " + inr_sign + str(rupees))