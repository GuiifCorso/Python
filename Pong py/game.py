from turtle import Turtle, Screen
import random
from gamescreen import Gamescreen
from scoreboard import Scoreboard
from pads import Pads
from ball import Ball
import time

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.tracer(0)


gamescreen = Gamescreen()
scoreboard = Scoreboard()
pads = Pads()
ball = Ball()

l_pad = pads.l_pad
r_pad = pads.r_pad

screen.listen()
screen.onkeypress(pads.pad_up, "w")
screen.onkeypress(pads.pad_down, "s")

game_is_on = True
ball.launch_ball()

while game_is_on:
    ball.move_ball()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce_ball()

    if ball.distance(l_pad) < 50 and ball.xcor() < 500 or ball.distance(r_pad) < 50 and ball.xcor() > -500:
        ball.x_bounce_ball()
        print(ball.heading())

    pads.follow_ball(ball.ycor())

    if ball.xcor() > 550:
        ball.reset_position()
        scoreboard.user_point()
        if ball.time > 0.005:
            ball.time -= 0.0005
        pads.r_pad_speed += 0.2
        ball.launch_ball()

    if ball.xcor() < -550:
        ball.reset_position()
        scoreboard.pc_point()
        if ball.time > 0.005:
            ball.time -= 0.0005
        pads.r_pad_speed += 0.2
        ball.launch_ball()

screen.exitonclick()