import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password too short"
    if not re.search(r'\d', password):
        return "Weak: Must contain at least one number"
    if not re.search(r'[A-Z]', password):
        return "Weak: Must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return "Weak: Must contain at least one lowercase letter"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Must contain at least one special character"
    return "Strong Password"

# Function to handle button click and show result
def on_check_password():
    password = entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place widgets
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show='*', width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=on_check_password)
button.pack(pady=10)

# Run the application
root.mainloop()
