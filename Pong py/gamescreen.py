from turtle import Turtle

class Gamescreen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.setheading(270)
        self.pensize(4)
        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)