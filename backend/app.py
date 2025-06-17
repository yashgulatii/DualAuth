from flask import Flask, render_template, request
import sqlite3
import os
from datetime import datetime

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.secret_key = 'supersecretkey'
DB_PATH = 'database/users.db'
LOG_PATH = 'database/injection_attempts.log'

def init_db():
    if not os.path.exists(DB_PATH):
        os.makedirs("database", exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("CREATE TABLE users (username TEXT, password TEXT)")
        c.executemany("INSERT INTO users (username, password) VALUES (?, ?)", [
            ('admin', 'admin123'),
            ('user1', 'password1'),
            ('guest', 'guest')
        ])
        conn.commit()
        conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login-vuln', methods=['GET', 'POST'])
def login_vulnerable():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        try:
            c.execute(query)
            result = c.fetchone()
            conn.close()
            if result:
                msg = "Login successful (vulnerable)"
            else:
                msg = "Login failed (vulnerable)"
        except Exception as e:
            msg = f"Error: {e}"

        with open(LOG_PATH, 'a') as log:
            log.write(f"{datetime.now()} | username='{username}', password='{password}'\n")
        return render_template('result.html', message=msg)
    return render_template('login_vulnerable.html')

@app.route('/login-safe', methods=['GET', 'POST'])
def login_secure():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()
        if result:
            msg = "Login successful (secure)"
        else:
            msg = "Login failed (secure)"
        return render_template('result.html', message=msg)
    return render_template('login_secure.html')

@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
