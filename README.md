# Ping-Pong-Game
A simple Ping Pong game built using Python's turtle graphics library. Players control paddles on either side of the screen to bounce a ball back and forth, attempting to score points by making the ball pass their opponent's paddle.

# Features
Two-player mode: Player 1 controls the left paddle, and Player 2 controls the right paddle.
Scoreboard: Keeps track of the score for both players.
Ball movement: The ball bounces off the paddles and walls. The ball's speed increases after each miss.

# Basic controls:
Player 1 (Left paddle): Use W to move up and S to move down.
Player 2 (Right paddle): Use the Up and Down arrow keys.

# Requirements
Python 3.x
turtle module (comes pre-installed with Python).

# Running the Game
Make sure you have the PING_PONG_CLASSES.py and README.md files in the same directory.

# Game Rules

The game is played between two players. Each player controls one paddle: the left player uses the Up and Down keys, and the right player uses the Up and Down arrow keys.
The objective of the game is to score by making the ball pass the opponent’s paddle.
The score is displayed at the top of the screen.
Each time a player misses the ball, the other player scores a point.
The ball resets to the center of the screen after every point.
The ball increases in speed after each point to make the game more challenging.
How It Works

The game is structured into several classes:

Ground: Defines the boundaries of the game.
ScoreBoard: Displays the score for both players.
Paddle: Controls the paddle's movement and position.
Ball: Controls the ball's movement, bouncing off the walls and paddles.
The turtle module is used to create graphics, allowing for interactive game development.
