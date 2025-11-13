import mysql.connector as m

con = m.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# Your data
l = ['shirsha', 17, 'A']

# Correct query (use %s for all placeholders)
sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"

# Execute the query
cur.execute(sql, l)

# Don’t forget to commit the change!
con.commit()

print("Data inserted successfully!")

# Close connection
con.close()
