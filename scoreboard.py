from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.update_score()


    def update_score(self):
        self.write(f"{self.score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
