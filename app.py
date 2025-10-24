from flask import Flask, request, render_template, redirect
import sqlite3
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reach_classa'


mysql = MySQL(app)


def init_db():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    email = request.form['email']
    message = request.form['Message']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO information (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    mysql.connection.commit()
    cur.close()

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
