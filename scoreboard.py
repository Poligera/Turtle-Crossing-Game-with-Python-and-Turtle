from turtle import Turtle
FONT = ("courier", 30, "bold")


class Score(Turtle):
    """An object inherited from Turtle class. It will show the current level of the game and when it's "game over"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-310, 280)
        self.color("black")
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(-140, 0)
        self.write("GAME OVER", font=FONT)