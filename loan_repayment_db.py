
import sqlite3
from datetime import datetime, timedelta

# Connect to or create the SQLite database
conn = sqlite3.connect('loan_repayments.db')
cursor = conn.cursor()

# Create a table to store loan repayment dates
cursor.execute('''
    CREATE TABLE IF NOT EXISTS loan_repayments (
        user_id INTEGER,
        repayment_date DATE,
        PRIMARY KEY (user_id, repayment_date)
    )
''')
conn.commit()

def add_repayment_date(user_id, repayment_date):
    cursor.execute('''
        INSERT INTO loan_repayments (user_id, repayment_date)
        VALUES (?, ?)
    ''', (user_id, repayment_date))
    conn.commit()

def get_repayment_dates(user_id):
    cursor.execute('SELECT repayment_date FROM loan_repayments WHERE user_id = ?', (user_id,))
    return [row[0] for row in cursor.fetchall()]

# Example usage
user_id = 1
repayment_date1 = datetime.now() + timedelta(days=7)   # Example: Repayment due in 7 days
repayment_date2 = datetime.now() + timedelta(days=14)  # Example: Repayment due in 14 days

# Add repayment dates
add_repayment_date(user_id, repayment_date1)
add_repayment_date(user_id, repayment_date2)
print("Repayment dates added successfully.")

# Retrieve repayment dates
repayment_dates = get_repayment_dates(user_id)
print("Repayment Dates for User ID {}: {}".format(user_id, repayment_dates))

# Close the database connection
conn.close()
