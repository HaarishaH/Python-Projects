from turtle import Turtle


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

    # def startservice(self, s1,s2):
    #  choice = self.ball.screen.textinput("1st Service", "Who wants to do the 1st service? (1 or 2)")
    #  if choice == "1":
    #      s1()
    #  elif choice == "2":
    #      s2()
    #  else:
    #      print("Invalid input. Defaulting to Player 1's service.")
    #      s1()


