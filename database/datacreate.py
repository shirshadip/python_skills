import mysql.connector as ms
con= ms.connect(
    host="localhost",
    user="root",
    passwd=""
)
cur = con.cursor()

sql = "DROP DATABASE data"
cur.execute(sql)
print ("database created successfully")
cur.execute("show databases")
for db in cur :
    print (db)
con.close()