# Simple Pong in Python 3 for Beginners
# Based on course by @TokyoEdTech
# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong by Knavels")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    # this will stop refreshing and updating the screen until we do it manually


# Main game loop
while True:
    wn.update() # every time the loop runs this update the screen
