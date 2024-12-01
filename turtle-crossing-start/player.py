from turtle import Turtle
from random import randint
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turt = Turtle()
        self.turt.shape('turtle')
        self.turt.color('white')
        self.turt.penup()
        self.turtstart()

    def turtstart(self):
        self.turt.setposition(STARTING_POSITION)
        self.turt.setheading(90)
    def turtmove(self):
        self.turt.fd(MOVE_DISTANCE)
    def dead(self):
        self.turt.shapesize(3)
        self.turt.color('red')


