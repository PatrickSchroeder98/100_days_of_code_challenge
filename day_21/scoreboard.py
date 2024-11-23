from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        """Updates the score text."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score."""
        self.score += 1
        self.update()

    # def game_over(self):
    #     """Shows the game over message."""
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.set_high_score()
        self.score = 0
        self.update()

    def set_high_score(self):
        """Sets the high score in file."""
        with open("data.txt", mode="w") as f:
            f.write(str(self.high_score))

    def get_high_score(self):
        """Gets the high score from file."""
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())
