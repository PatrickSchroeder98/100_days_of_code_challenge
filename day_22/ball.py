from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball."""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        """Bounces the ball on y axis."""
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball on x axis."""
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
