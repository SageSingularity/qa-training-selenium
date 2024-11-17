import sqlite3


def create_user(name, age, database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def update_user(name, age, database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("UPDATE users SET age = ? WHERE name = ?", (age, name))
    conn.commit()
    conn.close()

def delete_user(name, database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def get_user(name, database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_table(database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users", ())
    all_users = c.fetchall()
    conn.close()
    return all_users

def delete_users_from_user_table(database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()

def print_database(database_name):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)

def create_database(database_name):
    # Create a connection to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect(f'{database_name}.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table (if it doesn't exist)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
                )''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    print(f"SQLite database named {database_name} created successfully".format(database_name))