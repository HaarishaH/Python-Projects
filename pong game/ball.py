from turtle import Turtle
from random import randint,choice
from bat import Bat
class Ball:
    def __init__(self):
        self.ball = Turtle('circle')
        self.ball.color('white')
        self.ball.speed(1)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.x_move = 1
        self.y_move = 1
    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.bounce_x()

    def bal_disappear(self):
        self.ball.hideturtle()

