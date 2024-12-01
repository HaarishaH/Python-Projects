import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Score
from game_over import Game_over

screen = Screen()

screen.setup(width=600, height=650)
screen.bgcolor('grey')
screen.tracer(0)
player_obj = Player()
car_obj = Car()
score_obj = Score()
over_obj = Game_over()
screen.listen()
screen.onkeypress(player_obj.turtmove,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_obj.create_car()
    car_obj.carmove()

    for car in car_obj.c:
        if car.distance(player_obj.turt) < 20:
            score_obj.changecolor()
            player_obj.dead()
            screen.update()
            time.sleep(1)
            game_is_on = False
            over_obj.over()

    if player_obj.turt.ycor() >= 280:
        player_obj.turtstart()
        car_obj.carspeed()
        score_obj.update_score()
        score_obj.add_score()
        if score_obj.scorr >= 1:
            game_is_on = False
            over_obj.win()

screen.exitonclick()
