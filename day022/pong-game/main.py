from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # DETECT THE BALL'S COLLISION WITH THE UPPER AND LOWER WALLS
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH THE PADDLES
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # DETECT RIGHT PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # DETECT LEFT PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    game_is_on = not scoreboard.is_game_over()

screen.exitonclick()
