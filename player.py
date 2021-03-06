from turtle import Turtle
MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class inherited from Turtle class.
    Its methods control turtle's movement forward and check if it has crossed safely."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Setting the speed of the turtle:
    def cross_the_road(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # If successful, turtle goes back to the start for the next level:
    def is_crossing_successful(self):
        if self.ycor() > FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False