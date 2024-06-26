from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for turtle_index in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(starting_positions[turtle_index])
    segments.append(new_segment)

game_is_on = True
# while game_is_on:
#     screen.update()
#     for segment in segments:
#         segment.forward(20)
#         time.sleep(0.1)
#     segments[0].left(90)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_index in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_index - 1].xcor()
        new_y = segments[seg_index - 1].ycor()
        segments[seg_index].goto(new_x, new_y)
    segments[0].forward(20)
    # segments[0].left(90)


screen.exitonclick()
