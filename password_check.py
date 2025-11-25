import re   # Regular expressions to detect patterns

def check_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password.
    Returns: 'Weak', 'Moderate', or 'Strong'
    """
    # Criteria checks
    length_check = len(password) >= 8
    upper_check = re.search(r"[A-Z]", password) is not None
    lower_check = re.search(r"[a-z]", password) is not None
    digit_check = re.search(r"\d", password) is not None
    special_check = re.search(r"[@$!%*?&^#]", password) is not None  # common special characters

    # Count how many conditions are met
    score = sum([length_check, upper_check, lower_check, digit_check, special_check])

    # Decide strength
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
user_password = input("Enter a password to check its strength: ")
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")
