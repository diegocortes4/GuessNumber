import random

print("Welcome to the Number Guessing Game!\n")
print("I have chosen a number between 1 and 100.")
print("Can you guess what it is?")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
guess_count = 0
guess = 0

# Game loop
while guess != random_number:
    guess = input("Enter your guess: ").strip()

# Check if the input is a valid number
    if guess.isdigit():
        guess = int(guess)
        guess_count += 1

        if guess < 1 or guess > 100:
            print("Out of range! Please guess a number between 1 and 100.")
        elif guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number in", guess_count, "attempts.")
    else:
        print("Invalid input. Please enter a valid number between 1 and 100.")

# End of game message
print("\nCongratulations on finding the number!")
print("Thank you for playing!")