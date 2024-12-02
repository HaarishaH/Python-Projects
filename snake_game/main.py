
import time
from turtle import Screen
from boundary import Boundary
from snake import *
from food import *


object_screen = Screen()
object_screen.setup(width= 600 , height= 600)

object_screen.bgcolor("black")
object_screen.title(titlestring="My Snake Game")
object_screen.tracer(0)



snake_obj = Snake()
food_obj = Food()
boundary = Boundary()
object_screen.listen()
object_screen.onkey( snake_obj.up , "Up")
object_screen.onkey( snake_obj.right , "Right")
object_screen.onkey( snake_obj.left , "Left")
object_screen.onkey( snake_obj.down , "Down")

game_start = True
while game_start :
    object_screen.update()
    time.sleep(0.1)
    snake_obj.move()

    if snake_obj.head.distance(food_obj.object_food) <= 20:
        food_obj.spawn_food()
        snake_obj.update_snake()
        food_obj.object_score.add_score()

    if (snake_obj.head.xcor() > 280) | (snake_obj.head.xcor() < -280) | (snake_obj.head.ycor() > 280) | (snake_obj.head.ycor() < -280) :
        food_obj.trigger()
        snake_obj.re_create_snake()
    if snake_obj.collision() :
        food_obj.trigger()
        snake_obj.re_create_snake()

object_screen.exitonclick()
