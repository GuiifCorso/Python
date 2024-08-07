from turtle import Turtle
import random
import time
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.time = 0.05

    def launch_ball(self):
        self.rand_heading = random.randint(-45, 45)
        if self.rand_heading == 180:
            self.launch_ball()
        self.setheading(self.rand_heading)
    
    def move_ball(self):
        time.sleep(self.time)
        self.forward(10)

    def x_bounce_ball(self):
        current_heading = self.heading()
        if current_heading > 0 and current_heading < 90 or current_heading > 180 and current_heading < 270:
            self.setheading(current_heading + 2*(current_heading - 90))
        self.setheading(current_heading - 2*(current_heading - 90))

    def y_bounce_ball(self):
        current_heading = self.heading()
        self.setheading(-current_heading)

    def reset_position(self):
        self.goto(0, 0)