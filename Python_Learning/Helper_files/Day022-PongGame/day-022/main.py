from turtle import Turtle, Screen
import time

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.setworldcoordinates(-400, -300, 400, 300)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


screen.listen()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

scoreboard = Scoreboard()
sleep = 0.1

game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    # Detect wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 30 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
        if sleep > 0.001:
            sleep -= 0.005

    # Detect out of bound
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.increase_score("right")

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.increase_score("left")

screen.exitonclick()