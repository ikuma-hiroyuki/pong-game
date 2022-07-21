from turtle import Turtle


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.sleep_time = 0.1
        self.move_speed = speed
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = self.move_speed
        self.y_move = self.move_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.sleep_time = 0.1
        self.bounce_x()
