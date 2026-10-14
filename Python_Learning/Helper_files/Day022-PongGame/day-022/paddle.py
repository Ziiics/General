from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(5, 1)
        self.speed(0)
        self.setposition(location)

    def go_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)