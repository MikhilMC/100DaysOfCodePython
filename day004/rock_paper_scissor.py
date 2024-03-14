import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:

    print(game_images[choice])
    print("Computer chose:")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if (
        choice == 0 and computer_choice == 2
    ) or (
        choice == 1 and computer_choice == 0
    ) or (
        choice == 2 and computer_choice == 1
    ):
        print("You won")
    elif choice == computer_choice:
        print("It's a draw")
    else:
        print("You lose")