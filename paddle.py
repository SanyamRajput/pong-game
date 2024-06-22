from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position,0)

    def paddle_up(self):
        y = self.ycor() + 20
        self.goto(0, y)

    def paddle_down(self):
        y = self.ycor() - 20
        self.goto(0, y)


