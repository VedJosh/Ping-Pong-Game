from turtle import Screen
from PING_PONG_CLASSES import Paddle, Ball, Ground, ScoreBoard
import time

# setting up the screen
screen = Screen()
screen.setup(width=1240,height=650)
screen.bgcolor('black')
screen.title('Ping Pong Game')
screen.tracer(0)

# setting up the paddle
paddle_left = Paddle('left')
paddle_left.create_paddle()
paddle_right = Paddle('right')
paddle_right.create_paddle()

# setting up the ball
ball = Ball()
timegap = 0.01

# ground of game
ground = Ground()

# score board of game
board = ScoreBoard()
board.write_score()

# setting up the key controls
screen.listen()

# keeping the game on and the ball to move until game is finished
is_game_on = True
paddles = (paddle_left,paddle_right)
paddle_in_action = paddle_left


while is_game_on:
    
    # maintaining the keys control
    screen.onkeypress(fun=paddle_in_action.up,key='Up')
    screen.onkeypress(fun=paddle_in_action.down,key='Down')
    # keep moving the ball
    ball.motion()
    time.sleep(timegap)
    screen.update()
    ball.bounce_wall()
    paddle_in_action = ball.bounce_paddle(paddles,paddle_in_action)
    if ball.paddle_miss():
        ball.goto(0,0)
        ball.step+=1
        if paddles.index(paddle_in_action) == 0 :
            board.player2_score += 1
            ball.setheading(180)
        else:
            board.player1_score += 1
            ball.setheading(0)
        board.write_score()
    
    screen.update()
    
screen.exitonclick()