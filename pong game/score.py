from turtle import Turtle

class Score:
    def __init__(self):
        self.current_score1 = Turtle()
        self.current_score1.color('white')
        self.current_score1.hideturtle()
        self.current_score1.penup()
        self.current_score1.goto(30,260)
        self.score1 = 0
        self.update_score1()
        self.current_score2 = Turtle()
        self.current_score2.color('white')
        self.current_score2.hideturtle()
        self.current_score2.penup()
        self.current_score2.goto(-45, 260)
        self.score2 = 0
        self.update_score2()

    def update_score1(self):
        self.current_score1.clear()
        self.current_score1.write(f" {self.score1}", align="left", font=("Times New Roman ", 50, "bold"))
    def update_score2(self):
        self.current_score2.clear()
        self.current_score2.write(f" {self.score2}", align="right", font=("Times New Roman ", 50, "bold"))

    def add_score1(self):
        self.score1 +=1
        self.update_score1()
    def add_score2(self):
        self.score2 +=1
        self.update_score2()
