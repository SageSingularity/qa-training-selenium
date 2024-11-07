import sqlite3


def create_user():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))

    conn.commit()
    conn.close()


def print_database():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)
    


def create_database():
    # Create a connection to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect('mydatabase.db')

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

    print("SQLite database created successfully!")
