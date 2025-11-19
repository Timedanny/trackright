import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO tickets (title, description, status, priority) VALUES (?, ?, ?, ?)",
            ('Login button not working', 'When a user clicks the login button, nothing happens.', 'Open', 'High')
            )
cur.execute("INSERT INTO tickets (title, description, status, priority) VALUES (?, ?, ?, ?)",
            ('Homepage slow to load', 'The main page takes over 5 seconds to render.', 'In Progress', 'Medium')
            )
connection.commit()
connection.close()
