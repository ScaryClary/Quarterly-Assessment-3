import sqlite3
import random
import tkinter as tk
from tkinter import messagebox



# Function to read the classes available in the database
def get_classes():
    conn = sqlite3.connect('programming_quiz.db')  # Connect to the database
    c = conn.cursor()

    # Retrieve the list of tables (representing classes)
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    # Extract class names (table names)
    classes = [table[0] for table in tables]
    
    conn.close()
    return classes

# Function to fetch questions for a given class
def get_questions_for_class(class_name):
    conn = sqlite3.connect('programming_quiz.db')
    c = conn.cursor()

    # Retrieve questions from the selected class
    c.execute(f"SELECT * FROM '{class_name}'")
    rows = c.fetchall()
    conn.close()

    return rows

# Function to start the quiz for a selected class
def start_quiz(class_name, root):
    questions = get_questions_for_class(class_name)

    if not questions:
        messagebox.showerror("Error", f"No questions found for the class: {class_name}")
        return

    # Shuffle the questions to randomize the order
    random.shuffle(questions)

    score = 0
    question_index = 0

    # Create the label for questions dynamically
    question_label = tk.Label(root, text="Question", font=("Arial", 14), wraplength=400)
    question_label.pack(pady=20)

    # Create buttons for the options dynamically
    option_buttons = [tk.Button(root, text=f"Option {i+1}", font=("Arial", 12)) for i in range(4)]
    for button in option_buttons:
        button.pack(pady=5)

    # Function to update the question and options
    def next_question():
        nonlocal score, question_index
        if question_index < len(questions):
            row = questions[question_index]
            question = row[1]  # Question text is in the second column
            options = row[2:6]  # Options are in columns 2-5
            correct_answer = row[6]  # Correct answer is in column 6

            # Update question label with the current question
            question_label.config(text=f"Question {question_index + 1}: {question}")

            # Update the text of option buttons
            for i, option in enumerate(options):
                option_buttons[i].config(text=option)

            # Function to check the answer
            def check_answer(selected_option):
                nonlocal score, question_index
                if selected_option == correct_answer:
                    score += 1
                question_index += 1
                if question_index < len(questions):
                    next_question()  # Move to the next question
                else:
                    messagebox.showinfo("Quiz Completed", f"Your final score: {score}/{len(questions)}")
                    root.quit()  # Close the quiz window

            # Assign check_answer function to each button
            for i, option in enumerate(options):
                option_buttons[i].config(command=lambda opt=option: check_answer(opt))

        else:
            messagebox.showinfo("Quiz Completed", f"Your final score: {score}/{len(questions)}")
            root.quit()  # Close the quiz window

    next_question()

# Function to start the class selection window
def select_class():
    classes = get_classes()

    if not classes:
        messagebox.showerror("Error", "No classes available in the database.")
        return

    # Create a new window for class selection
    class_window = tk.Toplevel(root)
    class_window.title("Select a Class")

    class_label = tk.Label(class_window, text="Select a class to take the quiz:", font=("Arial", 14))
    class_label.pack(pady=10)

    def on_class_select(class_name):
        class_window.destroy()  # Close the class selection window
        start_quiz(class_name, root)

    # Create buttons for each class
    for class_name in classes:
        class_button = tk.Button(class_window, text=class_name, font=("Arial", 12), command=lambda cn=class_name: on_class_select(cn))
        class_button.pack(pady=5)

# Main function to start the application window
def main():
    global root
    root = tk.Tk()
    root.title("Programming Quiz")

    root.geometry("600x400")
    root.resizable(False, False)

    # Welcome label
    welcome_label = tk.Label(root, text="Welcome to the Programming Quiz!", font=("Arial", 18))
    welcome_label.pack(pady=20)

    # Start button
    start_button = tk.Button(root, text="Start Quiz", font=("Arial", 14), command=select_class)
    start_button.pack(pady=20)

    # Run the main window loop
    root.mainloop()

if __name__ == "__main__":
    main()
