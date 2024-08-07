from turtle import Turtle

class Pads(Turtle):
    def __init__(self):
        super().__init__()
        self.l_pad = Turtle()
        self.r_pad = Turtle()
        self.l_pad.penup()
        self.r_pad.penup()
        self.l_pad.color("white")
        self.r_pad.color("white")
        self.l_pad.goto(-560, 0)
        self.r_pad.goto(560, 0)
        self.l_pad.shape("square")
        self.r_pad.shape("square")
        self.l_pad.shapesize(5, 0.7)
        self.r_pad.shapesize(5, 0.7)
        self.r_pad_speed = 5

    def pad_up(self):
        if self.l_pad.ycor() < 230:
            self.l_pad.sety(self.l_pad.ycor() + 10)

    def pad_down(self):
        if self.l_pad.ycor() > -230:
            self.l_pad.sety(self.l_pad.ycor() - 10)

    def follow_ball(self, ycor):
        if not self.r_pad.ycor() > 230 or not self.r_pad.ycor() < -230:
            if self.r_pad.ycor() < ycor:
                self.r_pad.sety(self.r_pad.ycor() + self.r_pad_speed)
            elif self.r_pad.ycor() > ycor:
                self.r_pad.sety(self.r_pad.ycor() - self.r_pad_speed)
