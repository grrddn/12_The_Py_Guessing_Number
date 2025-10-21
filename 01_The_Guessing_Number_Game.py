import random


def set_difficulty():
    """Esta función determina la dificultad del juego"""
    defficulty = input("Type 'easy' or 'hard': \n")
    if defficulty == 'easy':
        return 10
    elif defficulty == 'hard':
        return 5
    else:
        print("Invalid defficulty")


def guessing_game():
    """Esta función activa el juego completo de adivinar el número"""
    opportunities = set_difficulty()
    print(f"You have {opportunities} attemps to guess the number\n")
    random_number = random.randint(1, 100)
    while opportunities > 0:
        number_guess = int(input("Make a guess:"))
        if number_guess == random_number:
            print(f"You got it! The answer was {random_number}")
            opportunities = 0
        elif number_guess > random_number:
            print("Too high")
            opportunities -= 1
            print(f"You have {opportunities} attemps to guess the number\n")
        elif number_guess < random_number:
            print("Too low")
            opportunities -= 1
            print(f"You have {opportunities} attemps to guess the number\n")

    if opportunities == 0 and number_guess != random_number:
        print("You've run out of guesses, you lose.")
        opportunities = 0
    elif opportunities == 0 and number_guess == random_number:
        print("You got it! The answer was {random_number}")
        opportunities = 0


print("""

   Welcome To the Number Guessing Game!!

I'm Thinking of a number between 1 and 100.
Can you guess it?
""")

guessing_game()

