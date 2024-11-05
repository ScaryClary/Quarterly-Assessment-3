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

        # Ask the user which table to select
        try:
            table_choice = int(input("\nEnter the number of the table you want to view: ")) - 1
            selected_table = tables[table_choice][0]

            # Retrieve and print the data from the selected table
            c.execute(f"SELECT * FROM '{selected_table}'")
            rows = c.fetchall()

            # Print the data from the selected table
            if rows:
                print(f"\nData from the '{selected_table}' table:")
                for row in rows:
                    print(row)
            else:
                print(f"\nThe '{selected_table}' table is empty.")
        
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid table number.")
    
    else:
        print("No tables found in the database.")

    # Close the connection
    conn.close()

# Call the function to read data
read_database()