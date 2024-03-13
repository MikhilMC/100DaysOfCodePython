print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?")

score = 0
combined_name = name1.lower() + name2.lower()

score1 = 0
score1 += combined_name.count("t")
score1 += combined_name.count("r")
score1 += combined_name.count("u")
score1 += combined_name.count("e")

score2 = 0
score2 += combined_name.count("l")
score2 += combined_name.count("o")
score2 += combined_name.count("v")
score2 += combined_name.count("e")

score = score1 * 10 +  score2
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")