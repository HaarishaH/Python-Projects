
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("highscoredata.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-100, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.current_score} High Score: {self.high_score}", align="left", font=("Comic Sans ", 12, "normal"))


    def add_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()


    def highscore(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("highscoredata.txt", mode = 'w') as data:
                data.write(f"{self.current_score}")
        self.current_score = 0
        self.update_scoreboard()
