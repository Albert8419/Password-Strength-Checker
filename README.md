# Password-Strength-Checker
A simple tool that checks the strength of a password based on length, character variety, and common patterns.

Explanation of Code:

Regex (re) is used to identify patterns in the password such as numbers, uppercase, and special characters.
The check_password_strength function evaluates the password based on these criteria.
The program gives feedback on why the password is weak or confirms its strength.

To run the script: python3 password_checker.py

# Graphical interface script is under password_checker_gui.py

Install Tkinter: 

Tkinter comes pre-installed with Python in most distributions, so you shouldn't need to install anything extra. If it's not available, you can install it via:

sudo apt-get install python3-tk

How it Works:

The tkinter library is used to create a graphical window with a label, an input field (password field), and a button.
When the button is clicked, the on_check_password function is triggered, which checks the password strength and displays the result in a message box.

Running the GUI:
Run the program by typing:

python3 password_checker_gui.py

How Weak Passwords Are a Security Risk:

Weak passwords are a critical security vulnerability because they can be easily guessed or cracked using brute-force or dictionary attacks. Attackers often exploit weak passwords to gain unauthorized access to accounts, leading to data breaches, identity theft, or system compromise. The more predictable or short a password is, the easier it is for malicious actors to break in.

Best Practices Applied:

In the project, I applied several password strength criteria:

Minimum length of 8 characters (to prevent brute-force attacks).
Inclusion of uppercase, lowercase, numbers, and special characters, ensuring complexity.
Feedback to improve weak passwords.
These practices align with best practices to ensure password strength and reduce the chances of successful cyberattacks.
