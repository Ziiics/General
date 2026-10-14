from turtle import Turtle, Screen

R_DOWN = 315
L_DOWN = 225
L_UP = 135
R_UP = 45

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.score = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
