import time
from turtle import Screen
from player import Player
from car_manager import Car

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.tracer(0)
player_obj = Player()
car_obj = Car()
screen.listen()
screen.onkeypress(player_obj.turtmove,'Up')
a = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if a == 5:
        car_obj.create_car()
        a = 0
    a+=1
    car_obj.carmove()

    if player_obj.turt.ycor() >= 280:
         player_obj.turtstart()

screen.exitonclick()
