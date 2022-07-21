import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
# r_paddle
r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# l_paddle
l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball(10)

score_r = Scoreboard((100, 270))
score_l = Scoreboard((-100, 270))

gami_is_on = True
while gami_is_on:
    time.sleep(ball.sleep_time)
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

    # ボールが左右の壁にぶつかったら
    if ball.xcor() > 370:
        ball.reset_position()
        score_l.point()

    if ball.xcor() < -370:
        ball.reset_position()
        score_r.point()

screen.exitonclick()
