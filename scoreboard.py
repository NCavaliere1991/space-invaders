from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.penup()
        self.color("lime")
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(150, -280)
        self.write(f'Score: {self.score}', align='center', font=('comic Sans MS', 30, 'normal'))
        self.goto(-200, -280)
        self.write(f'Lives: {self.lives}', align='center', font=('comic Sans MS', 30, 'normal'))

    def point(self):
        self.clear()
        self.score += 100
        self.update()

    def lose_life(self):
        self.clear()
        self.lives -= 1
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align='center', font=('comic Sans MS', 30, 'normal'))
    
    def win(self):
        self.goto(0, 0)
        self.write("Congratulations! You win!", align='center', font=('comic Sans MS', 30, 'normal'))
