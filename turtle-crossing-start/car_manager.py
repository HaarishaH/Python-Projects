from turtle import Turtle
from random import choice, randint

colors = ["brown", "cyan", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class Car:
    def __init__(self):
        self.c = []
        self.car_speed = MOVE_INCREMENT
    def create_car(self):
        random_chance = randint(0,6)
        if random_chance == 1:
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
            car.fd(self.car_speed)
            if car.xcor() < -280:
                car.goto(340,choice([x for x in range(-250,250,30)]))

    def carspeed(self):
        self.car_speed += MOVE_INCREMENT

