import sqlite3

# Connect to or create the SQLite database
conn = sqlite3.connect('loan_disbursement.db')
cursor = conn.cursor()

# Create a table to store loan disbursement status
cursor.execute('''
    CREATE TABLE IF NOT EXISTS loan_disbursement (
        user_id INTEGER PRIMARY KEY,
        borrower_name TEXT,
        loan_amount REAL,
        disbursement_status TEXT
    )
''')
conn.commit()

def add_loan_disbursement(borrower_name, loan_amount):
    cursor.execute('''
        INSERT INTO loan_disbursement (borrower_name, loan_amount, disbursement_status)
        VALUES (?, ?, ?)
    ''', (borrower_name, loan_amount, 'Pending'))
    conn.commit()

def update_disbursement_status(loan_id, new_status):
    cursor.execute('''
        UPDATE loan_disbursement
        SET disbursement_status = ?
        WHERE loan_id = ?
    ''', (new_status, loan_id))
    conn.commit()

def get_loan_status(loan_id):
    cursor.execute('SELECT disbursement_status FROM loan_disbursement WHERE user_id = ?', (user_id,))
    return cursor.fetchone()

# Example usage
borrower_name = "John Doe"
loan_amount = 10000.0

# Add loan disbursement
add_loan_disbursement(borrower_name, loan_amount)
print("Loan disbursement added successfully.")

# Update disbursement status
loan_id = 1
new_status = "Approved"
update_disbursement_status(loan_id, new_status)
print("Loan disbursement status updated.")

# Retrieve loan status
status = get_loan_status(loan_id)
if status:
    print("Loan Disbursement Status:", status[0])
else:
    print("Loan disbursement not found for the given loan ID.")

# Close the database connection
conn.close()


