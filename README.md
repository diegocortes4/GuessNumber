# Guess the Number Game

## Overview

The **Guess the Number** game is a simple interactive Python program where the user attempts to guess a randomly generated number between **1 and 100**. The program provides feedback on whether the guess is too high, too low, or correct.

## Game Rules

1. The program selects a **random number** between **1 and 100**.
2. The user inputs their guess.
3. The program provides **feedback**:
   - "Too low! Try again."
   - "Too high! Try again."
   - "Correct! You guessed the number in X attempts."
4. The game continues until the user **correctly guesses the number**.
5. The final message displays the total number of attempts.

## How to Run the Program

### Prerequisites

- Install **Python 3.x** on your system.

### Steps to Run

1. **Download the Python script** (`guess_the_number.py`).
2. **Open a terminal or command prompt**.
3. **Navigate to the script's directory**:
   ```bash
   cd /path/to/your/script
   ```
4. **Run the script using Python**:
   ```bash
   python guess_the_number.py
   ```

## Example Game Flow

```
Welcome to the Number Guessing Game!
I have chosen a number between 1 and 100.
Can you guess what it is?

Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 63
Correct! You guessed the number in 3 attempts.

Congratulations on finding the number!
Thank you for playing!
```

## Notes

- The game **only accepts numbers** between **1 and 100**.
- If an invalid input is entered, the program prompts the user to enter a valid number.

Enjoy the game!
