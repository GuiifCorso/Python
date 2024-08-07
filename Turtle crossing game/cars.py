from turtle import Turtle
import random

INCREMENT_SPEED = 10


class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            random_color = (red, green, blue)
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 3)
            new_car.seth(180)
            random_ypos = random.randint(-250, 250)
            new_car.goto(415, random_ypos)
            new_car.color(random_color)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed = self.car_speed + INCREMENT_SPEED