from turtle import Screen
from enemies import Enemies
import time
from turret import Turret
from barriers import Barrier
from scoreboard import Scoreboard

enemy = "sprites/New Piskel.gif"
ship = "sprites/ship.gif"

screen = Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.addshape(enemy)
screen.addshape(ship)
screen.setup(width=600, height=600)
screen.tracer(0)

enemies = Enemies()
turret = Turret()
barriers = Barrier()
scoreboard = Scoreboard()


def check_player_collisions():

    for enemy in enemies.enemy_list:
        if turret.bullet:
            if turret.bullet.distance(enemy) < 20:
                enemies.kill(enemy)
                turret.destroy()
                scoreboard.point()

    for brick in barriers.barrier_list:
        if turret.bullet:
            if turret.bullet.distance(brick) < 20:
                barriers.destroy(brick)
                turret.destroy()

    if turret.bullet and enemies.enemy_bullet:
        if turret.bullet.distance(enemies.enemy_bullet) < 20:
            turret.destroy()
            enemies.destroy_enemy_bullet()


def check_out_of_bounds():
    if turret.bullet:
        if turret.bullet.ycor() > 280:
            turret.destroy()
    if enemies.enemy_bullet:
        if enemies.enemy_bullet.ycor() < -280:
            enemies.destroy_enemy_bullet()


def check_enemy_collisions():
    if enemies.enemy_bullet:
        if enemies.enemy_bullet.distance(turret) < 20:
            enemies.destroy_enemy_bullet()
            turret.reset_position()
            scoreboard.lose_life()

    for brick in barriers.barrier_list:
        if enemies.enemy_bullet:
            if enemies.enemy_bullet.distance(brick) < 20:
                barriers.destroy(brick)
                enemies.destroy_enemy_bullet()
                

def check_win():
    if enemies.enemy_list:
        return False
    else:
        scoreboard.win()
        return True


screen.listen()
screen.onkey(key="Right", fun=turret.move_right)
screen.onkey(key="Left", fun=turret.move_left)
screen.onkey(key="space", fun=turret.shoot)
playing = True


while playing:
    screen.update()
    time.sleep(.2)
    enemies.move()
    enemies.enemy_shoot()
    check_win()

    if turret.bullet:
        turret.player_bullet_move()

    if enemies.enemy_bullet:
        enemies.enemy_bullet_move()

    check_player_collisions()
    check_out_of_bounds()
    check_enemy_collisions()
    
    if check_win():
        playing=False
    
    if scoreboard.lives == 0:
        scoreboard.game_over()
        playing = False


screen.exitonclick()
