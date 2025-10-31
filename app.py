from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import sqlite3

app = Flask(__name__)

# --- MySQL Configuration ---
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reach_classa'

mysql = MySQL(app)

# --- SQLite Configuration ---
SQLITE_DB = 'local_messages.db'

def init_sqlite():
    conn = sqlite3.connect(SQLITE_DB)
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


# Home page with form
@app.route('/')
def index():
    return render_template('index.html')

# Submit form (stores to BOTH MySQL and SQLite)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    email = request.form['email']
    message = request.form['Message']

    # --- Save to MySQL ---
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO information (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    mysql.connection.commit()
    cur.close()

    # --- Save to SQLite ---
    conn = sqlite3.connect(SQLITE_DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    conn.close()
#change 
    return redirect(url_for('index'))

# List messages from MySQL
@app.route('/list')
def list_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM information")
    data = cur.fetchall()
    cur.close()
    return render_template('list.html', messages=data)


#login and than go to list 

# @app.route('/login')
# def list_data():
#     return render_template('login.html')




# Delete message from MySQL
@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM information WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('list_data'))

if __name__ == '__main__':
    init_sqlite()  # initialize SQLite DB
    app.run(debug=True)