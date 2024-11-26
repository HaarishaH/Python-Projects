from turtle import Turtle, Screen
class Bat:
    def __init__(self):
        self.bat1 = Turtle('square')
        self.bat2 = Turtle('square')
        self.bat_object()

    def bat_object(self):
        self.bat1.speed(0)
        self.bat1.setposition(710,50)
        self.bat1.shapesize(4,1)
        self.bat1.color('white')
        self.bat2.speed(0)
        self.bat2.setposition(-718, -50)
        self.bat2.shapesize(4, 1)
        self.bat2.color('white')

    def bat1_up(self):
            self.bat1.penup()
            a = self.bat1.ycor()
            if a < 280:
                self.bat1.sety(a+70)
    def bat1_down(self):
            self.bat1.penup()
            b = self.bat1.ycor()
            if b > -280:
                self.bat1.sety(b-70)
    def bat2_up(self):
            self.bat2.penup()
            c = self.bat2.ycor()
            if c < 280:
                self.bat2.sety(c+70)
    def bat2_down(self):
            self.bat2.penup()
            d = self.bat2.ycor()
            if d > -280:
                self.bat2.sety(d-70)




