from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
# r_paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# l_paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

gami_is_on = True
while gami_is_on:
    ball.move()
    screen.update()

screen.exitonclick()
