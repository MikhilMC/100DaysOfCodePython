from art import logo, vs
from game_data import data
from random import randint

def generate_random_index():
    """
    Generate a random index from the given data.
    """
    return randint(0, len(data))

def format_data(account):
    """
    Returns data of the account in a printable string format.
    """
    name1 = account["name"]
    description1 = account["description"]
    country1 = account["country"]
    return f"{name1}, a {description1}, from {country1}"

def compare_accounts(guess, followers1, followers2):
    """
    Compares the followers count and check whether the guess is correct or not.
    """
    if followers1 > followers2:
        return guess == "a"
    else:
        return guess == "b"

def game():
    game_over = False
    score = 0
    data_len = len(data)
    index1 = randint(0, data_len-1)
    index2 = 0
    while not game_over:
        print(logo)
        while index1 == index2:
            index2 = randint(0, data_len-1)

        follower_count1 = data[index1]["follower_count"]
        print(f"Compare A: {format_data(data[index1])}")

        print(vs)

        follower_count2 = data[index2]["follower_count"]
        print(f"Against B: {format_data(data[index2])}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare_accounts(guess, follower_count1, follower_count2)

        if result:
            score += 1
            index1 = index2
        else:
            game_over = True

    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

game()