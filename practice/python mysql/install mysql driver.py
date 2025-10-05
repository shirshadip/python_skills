import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="shirshadip",
    password="avra1234"
)
print(mydb)