import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

time_lapsed = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    # Create cars.
    time_lapsed += 0.1
    if time_lapsed >= random.random() * 3:
        time_lapsed = 0
        car.create_car()

    # Collision with cars.
    for _ in car.cars:
        if player.distance(_) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Level Up.
    if player.reset_position():
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()
