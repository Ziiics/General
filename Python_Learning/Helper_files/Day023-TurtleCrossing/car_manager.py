from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LOW_Y = -230
HIGH_Y = 200
LOW_X = -300
HIGH_X = 300

class CarManager:
    def __init__(self):
        self.ALL_CARS = []

    def create_car(self, x, y) -> Turtle:
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(1,2)
        car.setheading(180)
        car.goto(x, y)
        car.speed(STARTING_MOVE_DISTANCE)
        return car

    def new_level(self, level):
        for car in self.ALL_CARS:
            car.hideturtle()

        self.ALL_CARS = []
        num_of_cars = level * 8 - level

        car.speed += MOVE_INCREMENT

        for n in range(num_of_cars):
            random_x = random.randint(LOW_X, HIGH_X)
            random_y = random.randint(LOW_Y, HIGH_Y)
            car = self.create_car(random_x, random_y)
            self.ALL_CARS.append(car)

    def move_cars(self):
        for car in self.ALL_CARS:
            car.forward(MOVE_INCREMENT)

            if car.xcor() < LOW_X:
                car.goto(HIGH_X, car.ycor())
