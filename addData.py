import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('programming_quiz.db')  # Use a generic name for the database file
c = conn.cursor()

# Create a table for the quiz questions
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 4220" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 3850" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "FIN 3210" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 4210" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS "ECON 4990" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            answer TEXT) ''')
    conn.commit()