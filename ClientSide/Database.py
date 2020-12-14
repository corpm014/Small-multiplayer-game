import sqlite3

# Connecting to the databases
conn = sqlite3.connect('Users.db')
c = conn.cursor()

# Creating the table
c.execute("""CREATE TABLE IF NOT EXISTS USERS
            username text,
            email text,
            password text
            """)

conn.commit()

conn.close()