def server():
    import mysql.connector as m
    con=m.connect(
        host="localhost",
    user="root",
    password="",
    )
    cur=con.cursor()
    
    con.close()
    