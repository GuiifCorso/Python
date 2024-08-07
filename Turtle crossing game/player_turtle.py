from turtle import Turtle

START = (0, -270)

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START)
        self.setheading(90)
    
    def move_turtle(self):
        self.forward(10)

    def reset_pos(self):
        self.goto(START)