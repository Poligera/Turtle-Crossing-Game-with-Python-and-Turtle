from turtle import Turtle
import random
COLORS = ["blue", "green", "red", "yellow", "orange", "purple", "brown", "grey"]
MOVE_INCREMENT = 5
MOVE_DISTANCE = 10


class CarManager:
    """Creates a car using a Turtle class and appends it to a list of cars.
    The other two methods control car speed"""

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        # A counter to reduce frequency of cars appearing on the screen later on, so it's approx. 1 every 6 loops:
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def drive_faster(self):
        self.car_speed += MOVE_INCREMENT
        self.drive()