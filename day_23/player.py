from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def up(self):
        """Makes the turtle to move up."""
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def is_at_finish(self):
        """Method to detect if turtle is at finish line."""
        return True if self.ycor() > FINISH_LINE_Y else False

    def goto_start(self):
        """Makes the turtle to go to the starting position."""
        self.goto(STARTING_POSITION)
