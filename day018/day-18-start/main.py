import turtle as t
from random import choice, randint

turtle = t.Turtle()
t.colormode(255)

# turtle.shape("turtle")
# turtle.color("red")
# rectangle
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# dotted line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# polygons


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_pattern():
    for sides in range(3, 10):
        turtle.color(choice(colors))
        draw_shape(sides)


def random_walk():
    for _ in range(200):
        turtle.color(random_color())
        turtle.forward(10)
        turtle.setheading(choice(directions))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


colors = [
    "royal blue", "dodger blue", "dark cyan", "green", "lime",
    "green yellow", "yellow", "orange", "maroon", "salmon"
]
directions = [0, 90, 180, 270]

# draw_pattern()
turtle.pensize(1)
turtle.hideturtle()
turtle.speed(0)
# random_walk()
draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
