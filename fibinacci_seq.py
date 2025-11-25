def fibonacci(n):
    """Generate and display Fibonacci sequence up to n terms."""
    a, b = 0, 1  # First two Fibonacci numbers
    sequence = []  # List to store the sequence

    for _ in range(n):
        sequence.append(a)  # Add the current number to the list
        a, b = b, a + b     # Update a and b for the next term

    print("Fibonacci sequence:")
    print(sequence)

# Take input from the user
try:
    terms = int(input("Enter the number of terms: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")
