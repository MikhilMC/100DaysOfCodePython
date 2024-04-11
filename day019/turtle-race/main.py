from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []
# print(user_bet)

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=-y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! The {user_bet} is the winning turtle.")
            else:
                print(f"You have lost! The {winning_turtle} is the winning turtle.")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
