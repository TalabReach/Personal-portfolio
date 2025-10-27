from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # change this to anything secure

# ✅ MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''   # change this
app.config['MYSQL_DB'] = 'reach_classa'          # change this
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# ✅ Show all stall data
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email, message, date FROM stall ORDER BY id")
    stalls = cur.fetchall()
    cur.close()
    # 👇 render list.html instead of index.html
    return render_template('list.html', stalls=stalls)

# ✅ Delete data by ID
@app.route('/delete/<int:id>', methods=['POST'])
def delete_stall(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM stall WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        flash('Data deleted successfully!', 'success')
    except MySQLdb.Error as e:
        flash(f'Error: {e}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
