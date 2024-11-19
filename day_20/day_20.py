import time
from turtle import Screen
from snake import Snake

"""The full version of the Snake game is in 21th day."""

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.update()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
