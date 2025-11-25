def validate_email(email: str) -> bool:
    # Check if '@' is present exactly once
    if email.count('@') != 1:
        return False
    
    username, domain = email.split('@')

    # Username must not be empty
    if not username:
        return False

    # Domain must contain at least one '.' and not start/end with '.'
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False

    # No spaces allowed
    if ' ' in email:
        return False

    return True
# Example usage
print(validate_email("sahil@example.com"))   # ✅ True
print(validate_email("sahil@domain"))        # ❌ False (no dot in domain)
print(validate_email("sahil@@gmail.com"))    # ❌ False (multiple @)
print(validate_email("@gmail.com"))          # ❌ False (empty username)
print(validate_email("sahil@.com"))          # ❌ False (domain starts with dot)