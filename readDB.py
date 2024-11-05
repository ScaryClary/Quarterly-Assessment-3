import sqlite3

# Function to read data from the database and print table data
def read_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('programming_quiz.db')  # Replace with your database file if needed
    c = conn.cursor()

 # Retrieve and print the list of tables in the database
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    
    # Check if there are tables in the database
    if tables:
        print("Tables in the database:")
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table[0]}")
