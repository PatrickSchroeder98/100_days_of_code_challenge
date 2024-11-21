import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
            ball.distance(right_paddle) < 50
            and ball.xcor() > 320
            or ball.distance(left_paddle) < 50
            and ball.xcor() < -320
    ):
        ball.bounce_x()
        ball.ball_speed *= 0.9

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.ball_speed = 0.1
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.ball_speed = 0.1
        ball.reset()

screen.exitonclick()
