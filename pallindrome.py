def is_palindrome(text: str) -> bool:
    # Convert to lowercase to ignore case
    text = text.lower()

    # Remove spaces (optional if you want to handle phrases)
    text = text.replace(" ", "")

    # Compare string with its reverse
    return text == text[::-1]
print(is_palindrome("madam"))                  # ✅ True
print(is_palindrome("racecar"))                # ✅ True
print(is_palindrome("hello"))                  # ❌ False
print(is_palindrome("Never odd or even"))      # ✅ True (ignores spaces and case)