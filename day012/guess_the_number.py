from random import randint
from art import logo

EASY_GAME_LEVEL = 5
HARD_GAME_LEVEL = 10

def set_difficulty():
    """
    Sets the difficulty of the game. i.e. the number of attempts.
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return HARD_GAME_LEVEL
    elif difficulty == 'hard':
        return EASY_GAME_LEVEL
    
def check_answer(answer, guess, turns):
    """
    Check the answer with the guess, and returns the number of turns left
    """
    if guess < answer:
        print("Too low.")
        return turns -1
    elif guess > answer:
        print("Too high")
        return turns -1
    else:
        print(f"You got it! The number was {guess}")

def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the number is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()