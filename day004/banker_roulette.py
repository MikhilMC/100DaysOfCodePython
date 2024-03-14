import random
names_string = input("Enter the names with ', ' as seperator : \n")
names = names_string.split(", ")
choice = random.randint(0, len(names)-1)
print(f"{names[choice]} is going to buy the meal today!")