import re

def check_password_strength(password):
    # Define the criteria
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Check length
    if len(password) < min_length:
        return "Password is too short. It should be at least 8 characters long."

    # Check for uppercase letters
    if not has_upper:
        return "Password should have at least one uppercase letter."

    # Check for lowercase letters
    if not has_lower:
        return "Password should have at least one lowercase letter."

    # Check for digits
    if not has_digit:
        return "Password should have at least one digit."

    # Check for special characters
    if not has_special:
        return "Password should have at least one special character."

    return "Password is strong!"

# Test the function
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)