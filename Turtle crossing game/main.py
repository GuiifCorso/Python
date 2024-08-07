from turtle import Screen
from player_turtle import PlayerTurtle
from cars import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
screen.colormode(255)

player_turtle = PlayerTurtle()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_turtle.move_turtle, "w")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if player_turtle.distance(car) < 30:
            game_on = False
            scoreboard.game_over()

    if player_turtle.ycor() > 270:
        player_turtle.reset_pos()
        car_manager.level_up()
        scoreboard.level_up()
        scoreboard.score_update()


screen.exitonclick()