from turtle import Turtle

class Game_over:
    def __init__(self):
        self.gameover = Turtle()
        self.gameover.hideturtle()

    def over(self):
        self.gameover.color('black')
        self.gameover.penup()
        self.gameover.goto(-310, -35)
        self.gameover.write(f" GAME OVER", align="left", font=("Times New Roman ", 70, "bold"))






