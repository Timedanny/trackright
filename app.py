import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)',
                     (title, description, 'Open'))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)