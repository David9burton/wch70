import random
import time

# generate a random number between 1 and 10

number_to_guess = random.randint(1, 10)
attempts = 0

print("Welcome to the Guessing Game!")
time.sleep(1)
print("I have selected a number between 1 and 10. Try to guess it!")
time.sleep(2)
print("Type 'quit' or 'exit' to end the game.")

while True:
    user_input = input("Enter your guess: ").lower()
    attempts += 1

    if user_input == "quit" or user_input == "exit":
        print(f"Sorry, you gave up! The correct number was {number_to_guess}.")
        break
    try:
        user_guess = int(user_input)
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:
        print("Please enter a valid number or type 'quit' or 'exit' to end the game.")
