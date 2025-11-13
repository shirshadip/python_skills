from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",        # change to your MySQL username
    password="",  # change to your password
    database="webapp"
)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()

    return f"Data inserted successfully: {name}, {email}"

if __name__ == "__main__":
    app.run(debug=True)
