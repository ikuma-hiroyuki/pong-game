from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self, goto):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(goto)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()
