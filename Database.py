import sqlite3
import UsersFile

"""
This is where the server will connect to the db and do the login stuff etc.
"""

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


# Adds a user to the db
def add_user(user):
    with conn:
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (user.username, user.email, user.password))
        print(f"[DATABASE] {user.username} has been inserted")


# Remove a user from the db
def remove_user(user):
    with conn:
        c.execute("DELETE from users WHERE (?, ?, ?)", (user.username, user.email, user.password))
        print(f"[DATABASE] {user.username} has been removed")


# Prints out a user
def print_user(user):
    c.execute("SELECT * FROM users WHERE username=(?)", (user.username,))
    print(c.fetchone())
    return c.fetchone()


conn.close()