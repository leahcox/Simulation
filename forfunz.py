import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint
from numpy import int32

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
# 
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Cat Fun. Press the mouse (but not too fast)!"
width = 500
height = 500
rw.newDisplay(width, height, name)


################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("dog.bmp")

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right 
# initState = (x, y, dx, dy, lives, seconds)
initState = (width/2, height/2, 1, 1, 100, 0)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
