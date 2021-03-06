from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Score
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("white")
screen.title("                                                                    TURTLE CROSSING")
screen.tracer(0)

player = Player()
score = Score()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.cross_the_road, key="Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    # Creating a car:
    car_manager.create_car()
    car_manager.drive()

    # DETECT collision with a car:
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_on = False

    # DETECT a successful crossing:
    if player.is_crossing_successful():
        score.increase_level()
        car_manager.drive_faster()

screen.exitonclick()