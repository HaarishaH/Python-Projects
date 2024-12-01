from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Score:
    def __init__(self):
        self.s = Turtle()
        self.s.color('white')
        self.s.hideturtle()
        self.s.penup()
        self.s.goto(-270, 290)
        self.scorr = 0
        self.update_score()

    def update_score(self):
        self.s.clear()
        self.s.write(f" Level: {self.scorr}", align="left", font=("Times New Roman ", 10, "bold"))
    def add_score(self):
        self.scorr +=1
        self.update_score()

    def changecolor(self):
        self.s.color('green')
        self.s.goto(-30, -10)
