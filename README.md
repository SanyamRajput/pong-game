
# 2D Pong Game

## Introduction
This is a simple 2D Pong game implemented in Python using the Turtle graphics library. The game includes a basic GUI where two players can control paddles to hit a ball back and forth across the screen. The goal is to prevent the ball from hitting the edges of the screen while trying to score points by making the opponent miss.

## Features
- Two-player mode (one player controls each paddle).
- Simple controls using keyboard inputs.
- Basic collision detection and scoring mechanism.
- Uses Python's Turtle graphics for drawing and animation.

## Requirements
- Python 3.x
- Turtle graphics library (usually included in standard Python installations)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/SanyamRajput/pong-game.git
   ```
2. Navigate to the project directory:
   ```
   cd pong-game
   ```
3. Run the game:
   ```
   python pong_game.py
   ```

## How to Play
- Player 1 controls: W (up), S (down)
- Player 2 controls: Up arrow (up), Down arrow (down)
- The game starts automatically upon running the script.
- Use the paddles to hit the ball back and forth.
- Each time the ball hits the opponent's side, you score a point.
- The game ends when one player reaches the score limit (default is 5 points).

## Customization

### `ball.py`
- In `ball.py`, you can customize aspects related to the ball's behavior and appearance:
  - Ball color
  - Ball size
  - Ball movement patterns
  
  Example of where you might find these parameters:
  ```python
  # Example of ball color customization
  BALL_COLOR = "red"
  
  # Example of ball size customization
  BALL_SIZE = 20
  ```

### `paddle.py`
- In `paddle.py`, you can customize aspects related to the paddles:
  - Paddle color
  - Paddle size
  - Paddle movement speed
  
  Example of where you might find these parameters:
  ```python
  # Example of paddle color customization
  PADDLE_COLOR = "blue"
  
  # Example of paddle size customization
  PADDLE_WIDTH = 100
  PADDLE_HEIGHT = 20
  ```

### `scoreboard.py`
- In `scoreboard.py`, you can customize aspects related to the game scoreboard:
  - Score display format
  - Scoreboard position
  
  Example of where you might find these parameters:
  ```python
  # Example of scoreboard position customization
  SCOREBOARD_FONT = ("Courier", 24, "normal")
  SCOREBOARD_COLOR = "black"
  SCOREBOARD_POSITION = (0, 260)
  ```
  
## Known Issues
- No known major issues. Minor bugs may exist, especially related to edge cases in collision detection.

## Contributing
- Contributions are welcome! If you find any bugs or have suggestions for improvements, please create an issue or submit a pull request on GitHub.

## Acknowledgments
- Inspired by the classic Pong game.
- Built using Python's Turtle graphics library.

