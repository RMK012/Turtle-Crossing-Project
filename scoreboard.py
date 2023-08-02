from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-280, 280)
        self.write(f"Level: {self.level} ", move=False, align="center", font=FONT)
        self.hideturtle()

    def increase_level(self):
        self.level += 1
        self.write(f"Score: {self.level}", move=False, align="center", font=FONT)

    def lose(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"You lose!, your score is: {self.level}",  move=False, align="center", font=FONT)





