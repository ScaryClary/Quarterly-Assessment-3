import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('programming_quiz.db')  # Use a generic name for the database file
c = conn.cursor()
