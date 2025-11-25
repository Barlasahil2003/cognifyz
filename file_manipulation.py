from collections import Counter
import string

def count_words(filename):
    """Read a text file and count occurrences of each word."""
    try:
        with open(filename, "r") as file:
            text = file.read()  # Read the entire file content

        # Convert to lowercase and remove punctuation
        text = text.lower()
        for p in string.punctuation:
            text = text.replace(p, "")

        # Split text into words
        words = text.split()

        # Count occurrences of each word
        word_counts = Counter(words)

        # Display results in alphabetical order
        print("\nWord Counts (Alphabetical Order):")
        for word in sorted(word_counts):
            print(f"{word} : {word_counts[word]}")

    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found. Please check the name and try again.")

# Ask the user for the file name
filename = input("Enter the text file name (with extension, e.g., sample.txt): ")
count_words(filename)
