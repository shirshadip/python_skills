import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    # database="mydata"
)
cur = con.cursor()
sql = "insert into data values('shirshadip')"

cur.execute(sql)
con.commit()
con.close()