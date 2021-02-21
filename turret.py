from turtle import Turtle

class Turret(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("sprites/ship.gif")
        self.penup()
        self.goto(0, -225)
        self.bullet = None
        self.bullet_list = []

    def move_right(self):
        if self.xcor() < 270:
            self.forward(10)

    def move_left(self):
        if self.xcor() > -275:
            self.backward(10)

    def shoot(self):
        if not self.bullet_list:
            self.bullet = Turtle(shape='square')
            self.bullet.color('yellow')
            self.bullet.shapesize(stretch_len=.5, stretch_wid=.1)
            self.bullet.setheading(90)
            self.bullet.penup()
            self.bullet.goto(self.xcor(), self.ycor())
            self.bullet_list.append(self.bullet)

    def player_bullet_move(self):
        self.bullet.forward(15)

    def destroy(self):
        self.bullet_list.remove(self.bullet)
        self.bullet.hideturtle()
        self.bullet = None

    def reset_position(self):
        self.goto(0, -225)

