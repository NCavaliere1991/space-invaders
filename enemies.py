from turtle import Turtle
import random

class Enemies(Turtle):
    def __init__(self):
        super().__init__()
        self.enemy_list = []
        self.make_enemies()
        self.moving_right = True
        self.enemy_bullet = None
        self.move_speed = 0.1

    def make_enemies(self):
        x, y = -250, 250
        for i in range(5):
            for j in range(11):
                enemy = Turtle()
                enemy.shape("sprites/New Piskel.gif")
                enemy.penup()
                enemy.goto(x, y)
                self.enemy_list.append(enemy)
                x += 40
            x -= 440
            y -= 30


    def move(self):
        sorted_list = sorted(self.enemy_list, key=lambda x: x.xcor(), reverse=True)
        last_enemy = sorted_list[0]
        first_enemy = sorted_list[-1]
        if self.moving_right:
            if last_enemy.xcor() < 270:
                for enemy in self.enemy_list:
                    enemy.forward(3)
            else:
                for enemy in self.enemy_list:
                    enemy.sety(enemy.ycor() - 3)
                    self.moving_right = False
        else:
            if first_enemy.xcor() > -275:
                for enemy in self.enemy_list:
                    enemy.backward(3)
            else:
                for enemy in self.enemy_list:
                    enemy.sety(enemy.ycor() - 3)
                    self.moving_right = True

    def kill(self, dead):
        dead.hideturtle()
        self.enemy_list.remove(dead)


    def enemy_shoot(self):
        if not self.enemy_bullet:
            self.enemy_bullet = Turtle(shape='square')
            self.enemy_bullet.color('red')
            self.enemy_bullet.shapesize(stretch_len=.5, stretch_wid=.1)
            self.enemy_bullet.setheading(270)
            self.enemy_bullet.penup()
            random_enemy = random.choice(self.enemy_list)
            self.enemy_bullet.goto(random_enemy.xcor(), random_enemy.ycor())

    def enemy_bullet_move(self):
        self.enemy_bullet.forward(15)

    def destroy_enemy_bullet(self):
        self.enemy_bullet.goto(2000, 2000)
        self.enemy_bullet = None



