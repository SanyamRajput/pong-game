from turtle import Screen
from paddle import Paddle

scr = Screen()
scr.setup(800,600)
scr.bgcolor('black')
scr.title('Pong Game')
scr.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

scr.listen()
scr.onkey(r_paddle.paddle_up,'Up')
scr.onkey(r_paddle.paddle_down,'Down')
scr.onkey(l_paddle.paddle_up,'Up')
scr.onkey(l_paddle.paddle_down,'Down')



ongame = True
while ongame:
    scr.update()


scr.exitonclick()
