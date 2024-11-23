from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Class responsible for the Snake segments and its' movement."""

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Creates the first 3 segments of snake."""
        for position in START_POSITION:
            self.add_segment(position)

    def move(self):
        """Moves the snake by a constant distance."""
        for i in range(len(self.segments) - 1, 0, -1):
            tmp_x = self.segments[i - 1].xcor()
            tmp_y = self.segments[i - 1].ycor()
            self.segments[i].goto(tmp_x, tmp_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Makes the snake to face up if it's not facing down."""
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        """Makes the snake to face down if it's not facing up."""
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        """Makes the snake to face left if it's not facing right."""
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        """Makes the snake to face right if it's not facing left."""
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def extend(self):
        """Add new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """Creates a new segment."""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        """Resets the Snake."""
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
