import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirshadip_sql1234"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS mywebsite_db")
cursor.execute("USE mywebsite_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
""")

conn.commit()
conn.close()
