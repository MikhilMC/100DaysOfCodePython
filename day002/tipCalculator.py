#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
amount = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
tip_amount = amount * tip_percent
total_amount = amount + tip_amount
amount_per_person = total_amount / people
final_amount = round(amount_per_person, 2)
final_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${final_amount}")
