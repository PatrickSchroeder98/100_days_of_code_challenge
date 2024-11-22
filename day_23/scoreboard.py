from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update()

    def update(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Updates the level of game."""
        self.level += 1
        self.update()

    def game_over(self):
        """Displays the game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
