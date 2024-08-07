from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"w")
screen.onkey(snake.left ,"a")
screen.onkey(snake.down ,"s")
screen.onkey(snake.right ,"d")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_add()
        score.score_updater()
        snake.segment_append()

    if snake.head.xcor() == 300 or snake.head.xcor() == -300 or snake.head.ycor() == 300 or snake.head.ycor() == -300:
        score.reset()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()

screen.exitonclick()