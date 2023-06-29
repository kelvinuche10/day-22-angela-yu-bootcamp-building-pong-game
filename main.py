from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()


# setting up the screen
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.listen()
screen.tracer(0)

# creating the paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
right_score = ScoreBoard((-40, 270))
left_score = ScoreBoard((40, 270))

ball = Ball()

screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(right_paddle) < 70 and ball.xcor() > 320) or (ball.distance(left_paddle) < 70 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 390:
        screen.tracer(0)
        left_score.increase_score()
        ball.reset_ball()
        screen.update()

    if ball.xcor() < -390:
        screen.tracer(0)
        right_score.increase_score()
        ball.reset_ball()
        screen.update()
