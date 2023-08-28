import sqlite3
import sys

# Get input parameters from Asterisk
user_id = sys.argv[1]
user_name = sys.argv[2]
user_dob= sys.argv[3]
user_gender=sys.argv[4]
user_status=sys.argv[5]

# Connect to the SQLite database
conn = sqlite3.connect('financial_services.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS loan_applications (ID INTEGER PRIMARY KEY,Name TEXT,DOB DATE,Gender TEXT,Status TEXT)')


# Check if user already exists in the database
cursor.execute("SELECT COUNT(*) FROM loan_applications WHERE id = ?", (user_id,))
user_count = cursor.fetchone()[0]

if user_count == 0:
    # User doesn't exist, insert new user details into the database
    cursor.execute('INSERT INTO loan_applications (ID,Name, DOB, Gender, Status) VALUES(?,?,?,?,?)',(user_id,user_name,user_dob,user_gender,user_status))
    conn.commit()
    response = "User registered successfully."
else:
    response = "User already exists."

# Commit the changes and close the connection
conn.commit()
conn.close()
print(f'Response: {response}')
