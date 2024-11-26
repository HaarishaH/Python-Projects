from turtle import Turtle
class Over:
    def __init__(self):
        self.over = Turtle()
        self.over.hideturtle()
        self.player_1wins=Turtle()
        self.player_2wins=Turtle()
    def show_over(self):
        self.over.color('red')
        self.over.penup()
        self.over.goto(-450,-50)
        self.over.write(f" GAME OVER", align="left", font=("Times New Roman ", 100, "bold"))
    def dispplayer_1wins(self):
        self.over.hideturtle()
        self.over.color('white')
        self.over.penup()
        self.over.goto(-400, -150)
        self.player_1wins.write(f" Player 1 Wins", align="left", font=("Times New Roman ", 70, "bold"))
    def dispplayer_2wins(self):
        self.over.hideturtle()
        self.over.color('white')
        self.over.penup()
        self.over.goto(-400, -150)
        self.player_2wins.write(f" Player 2 Wins", align="left", font=("Times New Roman ", 70, "bold"))
