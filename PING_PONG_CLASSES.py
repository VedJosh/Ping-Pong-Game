from turtle import Turtle
from random import randint
from math import fabs

class Ground(Turtle):

    # setting up the ground of the game
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.up()
        self.pensize(4)
        self.shapesize(0.1)
        self.goto(-360,250)
        self.down()
        for i in range(4):
            if i%2==0:
                self.forward(720)
            else:
                self.forward(520)
            self.right(90)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        
    
    def write_score(self):
        self.clear()
        self.goto(-100,230)
        self.write(self.player1_score,align='center',font = ('Courier',80,'normal'))
        self.goto(100,230)
        self.write(self.player2_score,align='center',font = ('Courier',80,'normal'))

class Paddle():
    def __init__(self,side):
        self.paddle_elements = ()
        self.x_cor = (-350 * (side=='left') ) + (350 * (side=='right'))
    
    # create a paddle of 4 square turtles
    def create_paddle(self):
        step = -40
        for i in range(4):
            paddle_elem = Turtle('square')
            paddle_elem.up()
            paddle_elem.goto(self.x_cor,step)
            paddle_elem.color('white')
            step -= 20
            self.paddle_elements += (paddle_elem,)

    # moves the paddle up until it at the top most position
    def up(self):
        if self.paddle_elements[0].ycor() < 240:
            for paddle_element in self.paddle_elements:
                paddle_element.setheading(90)
                paddle_element.forward(30)
    
    # moves the paddle down until it at the bottom most position
    def down(self):
        if self.paddle_elements[-1].ycor() > -260:
            for paddle_element in self.paddle_elements:
                paddle_element.setheading(270)
                paddle_element.forward(30)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.up()
        self.step = 4
        self.setheading(randint(150, 210))

    # move the ball forward
    def motion(self):
        self.forward(self.step)        

    # returns True if the paddle miss the ball
    def paddle_miss(self):
        if self.xcor() > 350 or self.xcor() < -350:
            return True
        return False

    # bounces the ball when it hit the wall up or down
    def bounce_wall(self):
        if self.ycor() < -250 or self.ycor() > 250:
            self.setheading(360-self.heading())

    # bounces the ball when it hits the paddle and return the paddle to which control should be switched
    def bounce_paddle(self,paddles,paddle_in_action):
        for num in range(len(paddle_in_action.paddle_elements)):
            if self.distance(paddle_in_action.paddle_elements[num]) < 20:
                self.setheading(180-self.heading()-randint(1,10))
                return [paddle for paddle in paddles if paddle != paddle_in_action][0]
        return paddle_in_action
