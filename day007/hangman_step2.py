import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

guess = input("Guess a letter: ").lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
