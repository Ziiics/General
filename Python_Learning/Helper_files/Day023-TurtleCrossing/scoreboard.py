from turtle import Screen, Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0,40)
        self.write("Game Over!", align="center", font=FONT)
