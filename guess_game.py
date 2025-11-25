import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("🎉 Congratulations! You guessed it right!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
