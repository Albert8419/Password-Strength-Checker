import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password too short"
    
    # Check for digits
    if not re.search(r'\d', password):
        return "Weak: Must contain at least one number"
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak: Must contain at least one uppercase letter"
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak: Must contain at least one lowercase letter"
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Must contain at least one special character"
    
    return "Strong Password"

# Get user input
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
