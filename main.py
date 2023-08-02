import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision with car

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.clear()
            scoreboard.lose()

    if player.ycor() > FINISH_LINE_Y:
        scoreboard.clear()
        scoreboard.increase_level()
        player.goto(STARTING_POSITION)
        car_manager.level_up()





screen.exitonclick()
