import sqlite3

# Connecting to the databases
conn = sqlite3.connect('Users.db')
c = conn.cursor()

# Creating the table
c.execute("""CREATE TABLE IF NOT EXISTS users (
            username text,
            email text,
            password text
            )""")

conn.commit()

# Testing
c.execute("INSERT INTO users VALUES (?, ?, ?)", ("hi","ho","he"))

conn.commit()

conn.close()