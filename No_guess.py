import random

print("🎯 Welcome to the Number Guessing Game!")

# Take the range input from the user
while True:
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
        if lower >= upper:
            print("⚠️ Upper bound must be greater than lower bound. Try again.")
            continue
        break
    except ValueError:
        print("⚠️ Please enter valid numbers for the range.")

# Generate a random number in the specified range
secret_number = random.randint(lower, upper)

print(f"\nI have selected a number between {lower} and {upper}. Can you guess it?")

attempts = 0  # To count the number of guesses

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment attempts

        # Check if guess is inside the given range
        if guess < lower or guess > upper:
            print(f"⚠️ Your guess must be between {lower} and {upper}. Try again.")
            continue

        # Give feedback to the user
        if guess < secret_number:
            print("Too low! 📉 Try again.")
        elif guess > secret_number:
            print("Too high! 📈 Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} attempts!")
            break
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
