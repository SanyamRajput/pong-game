from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(800, 600)
scr.bgcolor('black')
scr.title('Pong Game')
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(r_paddle.paddle_up, 'Up')
scr.onkey(r_paddle.paddle_down, 'Down')
scr.onkey(l_paddle.paddle_up, 'w')
scr.onkey(l_paddle.paddle_down, 's')

ongame = True
while ongame:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

scr.exitonclick()
