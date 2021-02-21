from turtle import Turtle

class Barrier(Turtle):
    def __init__(self):
        super().__init__()
        self.barrier_list = []
        self.barrier1()
        self.barrier2()
        self.barrier3()
        self.barrier4()

    def barrier1(self):
        x, y = -250, -175
        for i in range(3):
            for j in range(3):
                barrier = Turtle()
                barrier.color('lime')
                barrier.shape('square')
                barrier.penup()
                barrier.goto(x, y)
                self.barrier_list.append(barrier)
                x += 20
            x -= 60
            y += 20

    def barrier2(self):
        x, y = -100, -175
        for i in range(3):
            for j in range(3):
                barrier = Turtle()
                barrier.color('lime')
                barrier.shape('square')
                barrier.penup()
                barrier.goto(x, y)
                self.barrier_list.append(barrier)
                x += 20
            x -= 60
            y += 20

    def barrier3(self):
        x, y = 50, -175
        for i in range(3):
            for j in range(3):
                barrier = Turtle()
                barrier.color('lime')
                barrier.shape('square')
                barrier.penup()
                barrier.goto(x, y)
                self.barrier_list.append(barrier)
                x += 20
            x -= 60
            y += 20

    def barrier4(self):
        x, y = 200, -175
        for i in range(3):
            for j in range(3):
                barrier = Turtle()
                barrier.color('lime')
                barrier.shape('square')
                barrier.penup()
                barrier.goto(x, y)
                self.barrier_list.append(barrier)
                x += 20
            x -= 60
            y += 20

    def destroy(self, brick):
        brick.hideturtle()
        self.barrier_list.remove(brick)