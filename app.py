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

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    # Get single ticket to be edited
    conn = get_db_connection()
    ticket = conn.execute('SELECT * FROM tickets WHERE id = ?', (id,)).fetchone()
    conn.close()

    # Handle form submission
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']

        conn = get_db_connection()
        conn.execute('UPDATE tickets SET title = ?, description = ?, status = ? WHERE id = ?',
                     (title, description, status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('edit.html', ticket=ticket)

if __name__ == '__main__':
    app.run(debug=True)