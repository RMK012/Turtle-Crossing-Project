# Turtle Crossing Game

This project is a simple and fun game that's been implemented using Python's `turtle` module. It's a variation of the classic "Frogger" game, with a turtle trying to cross a busy street. 

## Gameplay

The player controls a turtle, moving it upwards in an attempt to cross a street full of cars. The cars are moving horizontally across the screen at varying speeds and intervals. The objective is to reach the top of the screen without colliding with any of the cars. If the player reaches the top, the level increases and the player starts again from the bottom. The game ends if the turtle collides with a car. 

## Code Structure

The code is split into several Python files, each representing a different aspect of the game:

- `main.py`: The main game loop is located in this file. It sets up the game screen, creates the player and the car manager, and handles the main loop that updates the screen and moves the cars.

- `player.py`: This file defines the `Player` class, which is responsible for player movement.

- `car_manager.py`: This file defines the `CarManager` class, which is responsible for creating and moving the cars on the screen.

- `scoreboard.py`: This file defines the `Scoreboard` class, which handles displaying the player's current level on the screen.

## How to Run the Game

To run the game, simply execute the `main.py` file in a Python environment that has the `turtle` module available. This will start the game. You can control the turtle using the "Up" key on your keyboard.

---

