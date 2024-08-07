import turtle
from colors import color_list
import random

john = turtle.Turtle()
john.shape('turtle')
john.penup()
john.hideturtle()
john.teleport(-250, -250)
john.speed(0)

def draw_dots(size):

    for _ in range(size):
        for _ in range(size):
            rand_color = random.choice(color_list)
            john.dot(20, rand_color)
            john.forward(50)
        john.teleport(-250, john.ycor() + 50)



screen = turtle.Screen()
screen.colormode(255)
screen.screensize(450, 500)
draw_dots(10)
screen.exitonclick()


