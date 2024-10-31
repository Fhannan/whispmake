import sqlite3

# Function to create the database and the table
def create_table():
    conn = sqlite3.connect('friends.db')  # This will create a file named friends.db
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            email TEXT,
            mobile TEXT,
            location TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a friend to the database
def add_friend(name, address, email, mobile, location, description):
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO friends (name, address, email, mobile, location, description) VALUES (?, ?, ?, ?, ?, ?)',
                   (name, address, email, mobile, location, description))
    conn.commit()
    conn.close()

# Function to retrieve all friends from the database
def get_friends():
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM friends')
    friends = cursor.fetchall()  # Fetch all records
    conn.close()
    return friends  # Return the list of friends

# Function to retrieve a friend by their ID
def get_friend_by_id(friend_id):
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM friends WHERE id = ?', (friend_id,))
    friend = cursor.fetchone()  # Fetch the first matching record
    conn.close()
    return friend  # Return friend details as a tuple

# Function to remove a friend by their ID
def delete_friend(friend_id):
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM friends WHERE id = ?', (friend_id,))
    conn.commit()
    conn.close()


def delete_all_friends():
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM friends')
    conn.commit()
    conn.close()

def get_total_friends():
    conn = sqlite3.connect('friends.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM friends')  # Use COUNT to get the number of friends
    total = cursor.fetchone()[0]  # Fetch the total count
    conn.close()
    return total
