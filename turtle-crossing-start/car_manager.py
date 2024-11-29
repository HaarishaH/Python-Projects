from turtle import Turtle
from random import choice

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    def __init__(self):
        self.c = []
    def create_car(self):
        car = Turtle('square')
        car.color(choice(colors))
        car.shapesize(1,2)
        car.penup()
        car.setheading(180)
        y = choice([x for x in range(-250,250,30)])
        car_start_position = (340, y)
        car.goto(car_start_position)
        self.c.append(car)

    def carmove(self):
        for car in self.c:
            car.fd(MOVE_INCREMENT)
            if car.xcor() < -280:
                car.goto(340,choice([x for x in range(-250,250,30)]))


