from turtle import Turtle

class Game_over:
    def __init__(self):
        self.gameover = Turtle()
        self.gameover.hideturtle()
        self.won = Turtle()
        self.won.hideturtle()


    def over(self):
        self.gameover.color('black')
        self.gameover.penup()
        self.gameover.goto(-310, -35)
        self.gameover.write(f" GAME OVER", align="left", font=("Times New Roman ", 70, "bold"))

    def win(self):
        self.won.color('green')
        self.won.penup()
        self.won.goto(-250, -35)
        self.won.write(f" YOU WON", align="left", font=("Times New Roman ", 70, "bold"))






