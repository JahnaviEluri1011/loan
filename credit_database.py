import sqlite3

# Connect to or create the SQLite database
conn = sqlite3.connect('credit_database.db')
cursor = conn.cursor()

# Create a table to store credit details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS credit_details (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        credit_score INTEGER,
        credit_limit REAL
    )
''')
conn.commit()

def add_credit_details(user_id, name, credit_score, credit_limit):
    cursor.execute('''
        INSERT INTO credit_details (user_id, name, credit_score, credit_limit)
        VALUES (?, ?, ?, ?)
    ''', (user_id, name, credit_score, credit_limit))
    conn.commit()

def get_credit_details(user_id):
    cursor.execute('SELECT * FROM credit_details WHERE user_id = ?', (user_id,))
    return cursor.fetchone()

# Example usage
user_id = 1
name = "John Doe"
credit_score = 750
credit_limit = 10000.0

# Add credit details
add_credit_details(user_id, name, credit_score, credit_limit)
print("Credit details added successfully.")

# Retrieve credit details
retrieved_details = get_credit_details(user_id)
if retrieved_details:
    print("Credit Details:")
    print("User ID:", retrieved_details[0])
    print("Name:", retrieved_details[1])
    print("Credit Score:", retrieved_details[2])
    print("Credit Limit:", retrieved_details[3])
else:
    print("Credit details not found for the given user ID.")

# Close the database connection
conn.close()
