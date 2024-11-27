from turtle import Turtle, Screen
from bat import Bat
from ball import Ball
from score import Score
from gameover import Over
from random import randint
screen = Screen()
screen.setup(width= 1500 , height= 700)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
court = Turtle()
court.color('white')
court.speed(0)
court.pensize(8)
court.penup()
court.goto(735,340)
court.right(90)
court.pendown()
court.fd(675)
court.right(90)
court.fd(1475)
court.right(90)
court.fd(677)
court.right(90)
court.fd(1475)
court.penup()
court.goto(0,340)
court.right(90)
for i in range(11):
    court.pendown()
    court.forward(25)
    court.penup()
    court.fd(40)
    screen.tracer(0)

bat_obj = Bat()
ball_obj = Ball()
score_obj = Score()
over_obj = Over()
screen.listen()
screen.onkey(bat_obj.bat1_up,'Up')
screen.onkey(bat_obj.bat1_down,'Down')
screen.onkey(bat_obj.bat2_up,'w')
screen.onkey(bat_obj.bat2_down,'s')


while True:
    screen.update()
    ball_obj.move()
    if ball_obj.ball.ycor() > 320 or ball_obj.ball.ycor() < -320:
        ball_obj.bounce_y()
    if abs(ball_obj.ball.xcor() - bat_obj.bat1.xcor()) < 20 and abs(ball_obj.ball.ycor() - bat_obj.bat1.ycor()) < 50:
        ball_obj.bounce_x()
    if abs(ball_obj.ball.xcor() - bat_obj.bat2.xcor()) < 20 and abs(ball_obj.ball.ycor() - bat_obj.bat2.ycor()) < 50:
        ball_obj.bounce_x()

    if ball_obj.ball.xcor() > 720:
        ball_obj.reset_position()
        score_obj.update_score2()
        score_obj.add_score2()
        if score_obj.score2 >= 2:
            ball_obj.bal_disappear()
            over_obj.show_over()
            over_obj.dispplayer_2wins()
            break
    if ball_obj.ball.xcor() < -720:
        ball_obj.reset_position()
        score_obj.update_score1()
        score_obj.add_score1()
        if score_obj.score1 >= 2:
            ball_obj.bal_disappear()
            over_obj.show_over()
            over_obj.dispplayer_1wins()
            break
screen.exitonclick()
