# Simple Pong in Python 3 for Beginners
# Based on course by @TokyoEdTech
# Part 1: Getting Started
# Part 2: Game Objects
# Part3: Moving the Paddles

import turtle

wn = turtle.Screen()
wn.title("Pong by Knavels")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    # this will stop refreshing and updating the screen until we do it manually

# everything is a Turtle object
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   # Maximum speed of drawing/turtle animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)   # resize shape to make it like a paddle
paddle_a.penup()    # stop drawing at the point we where
paddle_a.goto(-350, 0)  # go to the specific point

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   # Maximum speed of drawing/turtle animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)   # resize shape to make it like a paddle
paddle_b.penup()    # stop drawing at the point we where
paddle_b.goto(350, 0)  # go to the specific point

# Ball
ball = turtle.Turtle()
ball.speed(0)   # Maximum speed of drawing/turtle animation
ball.shape("square")
ball.color("white")
ball.penup()    # stop drawing at the point we where
ball.goto(0, 0)  # go to the center of the screen

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()     # listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")     # when key "w" is pressed run paddle_a_up
wn.onkeypress(paddle_a_down, "s")     # when key "s" is pressed run paddle_a_down
wn.onkeypress(paddle_b_up, "Up")     # when key "Up" is pressed run paddle_b_up
wn.onkeypress(paddle_b_down, "Down")     # when key "Down" is pressed run paddle_b_down


# Main game loop
while True:
    wn.update() # every time the loop runs this update the screen
