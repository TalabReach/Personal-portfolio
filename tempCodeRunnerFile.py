# def init_db():
#     conn = sqlite3.connect('database.sql')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS messages (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             message TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
# @app.route('/')
# def index():
#     return render_template('index.html')  

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['Name']
#     email = request.form['email']
#     message = request.form['Message']

#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO information (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
#     mysql.connection.commit()
#     cur.close()

#     return render_template('index.html')