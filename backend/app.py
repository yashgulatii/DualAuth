from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import os
from datetime import datetime

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.secret_key = 'supersecretkey'
DB_PATH = 'database/users.db'
LOG_PATH = 'logs/injection_attempts.log'

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute(query)
            result = c.fetchone()
            conn.close()

            with open(LOG_PATH, 'a') as log:
                log.write(f"{datetime.now()} | SQLi Attempt | username='{username}', password='{password}'\n")

            if result:
                session['username'] = username
                session['mode'] = 'vulnerable'
                return redirect(url_for('dashboard'))
            else:
                return render_template('result.html', message="Login failed (vulnerable)")
        except Exception as e:
            return render_template('result.html', message=f"Error: {e}")
    return render_template('login_vulnerable.html')

@app.route('/login-safe', methods=['GET', 'POST'])
def login_secure():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            session['username'] = username
            session['mode'] = 'secure'
            return redirect(url_for('dashboard'))
        else:
            return render_template('result.html', message="Login failed (secure)")
    return render_template('login_secure.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username', 'Unknown')
    mode = session.get('mode', 'secure')

    # Assume a basic check that SQLi-style bypass likely happened
    hacked = (mode == 'vulnerable' and "'" in username)

    return render_template('dashboard.html', username=username, hacked=hacked)


@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
