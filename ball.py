from turtle import Turtle
import random


rand_ycor = random.randint(-280, 280)
rand_xcor = random.randint(-380, 380)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.y_move = 10
        self.x_move = 10
        self.move_time = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_time *= 0.9 

    def reset_ball(self):
        self.move_time = 0.1
        self.goto(0,0)
        self.bounce_x()

        


        
        
