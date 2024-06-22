from turtle import Turtle,Screen

scr = Screen()
scr.setup(800,600)
scr.bgcolor('black')
scr.title('Pong Game')

paddle = Turtle() 
paddle.color('white')
paddle.shape('square')
paddle.shapesize(stretch_wid=5, stretch_len=1)        
paddle.goto(350,0)       
paddle.listen()




scr.exitonclick()
