from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_points = 0
        self.pc_points = 0
        self.user_score = Turtle()
        self.pc_score = Turtle()
        self.user_score.penup()
        self.pc_score.penup()
        self.user_score.hideturtle()
        self.pc_score.hideturtle()
        self.user_score.goto(-75, 180)
        self.pc_score.goto(75, 180)
        self.user_score.color("white")
        self.pc_score.color("white")
        self.user_score.write(f"{self.user_points}", False, "center", ("Arial", 78, "bold"))
        self.pc_score.write(f"{self.pc_points}", False, "center", ("Arial", 78, "bold"))

    def pc_point(self):
        self.pc_score.clear()
        self.pc_points += 1
        self.pc_score.write(f"{self.pc_points}", False, "center", ("Arial", 78, "bold"))

    def user_point(self):
        self.user_score.clear()
        self.user_points += 1
        self.user_score.write(f"{self.user_points}", False, "center", ("Arial", 78, "bold"))