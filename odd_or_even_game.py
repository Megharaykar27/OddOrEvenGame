import random

def odd_or_even_game():
    print("Welcome to the Odd or Even Game!")
    print("I will generate a number, and you have to guess if it's odd or even.")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Get the player's guess
    player_guess = input("Guess if the number is 'odd' or 'even': ").lower()

    # Check if the player's guess is valid
    if player_guess not in ['odd', 'even']:
        print("Invalid input! Please type 'odd' or 'even'.")
        return

    # Determine if the number is odd or even
    if number % 2 == 0:
        correct_answer = "even"
    else:
        correct_answer = "odd"

    # Display the number and the result
    print(f"The number is {number}.")
    if player_guess == correct_answer:
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")

if __name__ == "__main__":
    odd_or_even_game()
