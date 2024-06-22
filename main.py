from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

scr = Screen()
scr.setup(800,600)
scr.bgcolor('black')
scr.title('Pong Game')
scr.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scr.listen()
scr.onkey(r_paddle.paddle_up,'Up')
scr.onkey(r_paddle.paddle_down,'Down')
scr.onkey(l_paddle.paddle_up,'w')
scr.onkey(l_paddle.paddle_down,'s')


ongame = True
while ongame:
    time.sleep(0.1)
    scr.update()
    ball.move()


scr.exitonclick()
