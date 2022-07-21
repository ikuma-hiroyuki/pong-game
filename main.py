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

    # 上下の壁にぶつかったら反射
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # パドルにぶつかったら反射
    hitting_x = (ball.distance(r_paddle) < 50 and ball.xcor() > 330)
    hitting_y = (ball.distance(l_paddle) < 50 and ball.xcor() < -330)
    if hitting_x or hitting_y:
        ball.bounce_x()

screen.exitonclick()
