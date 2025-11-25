def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("hello"))  # Output: olleh
