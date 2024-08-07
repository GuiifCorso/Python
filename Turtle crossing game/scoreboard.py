from turtle import Turtle
import time

FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-330, 250)
        self.write(f"Score: {self.level}", False, "center", FONT)
    
    def score_update(self):
        self.goto(-330, 250)
        self.level += 1
        self.clear()
        self.write(f"Score: {self.level}", False, "center", FONT)

    def game_over(self):
        self.level = 0
        self.clear()
        self.goto(0, 0)
        self.write("Game over", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.goto(0, 0)
        self.write("Level up!", False, "center", FONT)
        time.sleep(1)
        self.clear()