from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1
        self.goto(x=new_x, y=new_y)