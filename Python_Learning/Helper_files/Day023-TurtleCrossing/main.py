import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300)
screen.tracer(0)

user = Player()
scoreboard = Scoreboard()
the_car = CarManager()
level = 1

screen.listen()
screen.onkey(user.up, "Up")

game_is_on = True
the_car.new_level(level)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    the_car.move_cars()

    # user reach the end
    if user.ycor() > 278:
        level += 1
        scoreboard.update_score()
        the_car.new_level(level)

    # if user hit the car
    for car in the_car.ALL_CARS:
        if user.distance(car) < 23:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()