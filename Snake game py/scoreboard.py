from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", False, "center", ("Arial", 24, "normal"))

    def score_updater(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}" , False, "center", ("Arial", 24, "normal"))

    def score_add(self):
        self.score += 1

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.score_updater()