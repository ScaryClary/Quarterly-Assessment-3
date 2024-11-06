import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to open the quiz window and display questions
def open_quiz_window(category):
    quiz_window = tk.Toplevel()
    quiz_window.title(f"{category} Quiz")
    
    conn = sqlite3.connect('quiz.db')  # Replace with your actual database file path
    cursor = conn.cursor()
    
    # Fetch questions from the selected category (table)
    cursor.execute(f"SELECT question, option1, option2, option3, option4, correct_answer FROM '{category}' LIMIT 10")
    questions = cursor.fetchall()
    
    # Store the current question index
    current_question_idx = 0
    score = 0

    def load_question():
        nonlocal current_question_idx, score
        if current_question_idx < len(questions):
            # Get the current question and options
            question, opt1, opt2, opt3, opt4, correct_answer = questions[current_question_idx]
            
            # Display the question
            question_label.config(text=f"Q{current_question_idx + 1}: {question}")
            
            # Update the radio button options
            radio_var.set(None)  # Clear previous selection
            option1_button.config(text=opt1, value=opt1)
            option2_button.config(text=opt2, value=opt2)
            option3_button.config(text=opt3, value=opt3)
            option4_button.config(text=opt4, value=opt4)
            
            # Save the correct answer
            correct_answer_label.config(text=correct_answer)
        else:
            # End of quiz, display the score
            messagebox.showinfo("Quiz Complete", f"You've completed the quiz! Your score: {score}/{len(questions)}")
            quiz_window.destroy()

    def submit_answer():
        nonlocal current_question_idx, score
        selected_answer = radio_var.get()
        correct_answer = correct_answer_label.cget("text")
        
        if selected_answer == correct_answer:
            score += 1
        
        current_question_idx += 1
        load_question()

    # UI Setup
    question_label = tk.Label(quiz_window, text="", wraplength=400, justify="left")
    question_label.pack(pady=10)

    radio_var = tk.StringVar()

    option1_button = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    option1_button.pack(anchor="w")

    option2_button = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    option2_button.pack(anchor="w")

    option3_button = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    option3_button.pack(anchor="w")

    option4_button = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    option4_button.pack(anchor="w")

    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack(pady=10)

    # Hidden label to store the correct answer
    correct_answer_label = tk.Label(quiz_window, text="", fg="grey")
    correct_answer_label.pack_forget()  # Hide this label

    load_question()  # Load the first question

    # Close the connection
    conn.close()

