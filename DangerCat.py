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
# The state of the cat is represented by a tuple (pos, delta-pos, lives).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop. The third
# element, 'lives', counts the number of attempts remaining to play the
# game.
#
# For example, the tuple (7,1,2) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick," with two
# lives remaining.
# 
# The initial state of the cat in this program is (0,1,3), meaning that the cat
# starts at the left of the screen and moves right one pixel per
# tick. It starts with three lives.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# One of the lives is lost when the cat is allowed to reach any edge
# of the screen.
# The simulation ends when all three lives have been lost.

################################################################

# Initialize world
name = "Click the mouse to keep the cat alive. Don't let it run off the screen!"
width = 500
height = 500
rw.newDisplay(width, height, name)


################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple, with
# three lives
# Display a count of the number of remaining lives and the duration of
# the game (how many minutes and seconds the cat has been kept alive)
#
#state = (300, 200, 2, 1, 3)

def updateDisplay(state):
    lifeDisplay= dw.makeLabel("Remaining lives:"+str(state[4]), "serif", 18, (0, 0, 0))
    timeDisplay= dw.makeLabel("Time:0"+str(state[5]//3600)+":"+str((state[5]//60)%60), "serif", 18, (0,0,0))
    if (150<=state[0]<=350 and 150<=state[1]<=350):
        dw.fill(dw.green)
        dw.draw(myimage, (state[0],state[1]))
    elif(50<=state[0]<=450 and 50<=state[1]<=450):
        dw.fill(dw.yellow)
        dw.draw(myimage, (state[0], state[1]))
    else:
        dw.fill(dw.red)
        dw.draw(myimage, (state[0], state[1]))
    dw.draw(lifeDisplay, (20, 15))
    dw.draw(timeDisplay, (20, 35))
################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# state -> state
def updateState(state):
    if (state[0] > width or state[0] < -100 or state[1] > height or state[1] < -100):
        newlife = state[4] - 1
        secondState = (width/2, height/2, 1, 1, newlife, state[5])
        return secondState
    else:
        secondState = (state[0]+state[2],state[1]+state[3],state[2],state[3],state[4],state[5]+1)
        return secondState
################################################################

# Remove a life when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen
# width or height. Terminate the simulation when the number of lives,
# represented by state[4], is equal to zero.
# state -> bool
def endState(state):
    if (state[4] == 0):
        return True
    else:
        return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat's
# direction. The background of the game changes color to reflect the
# position of the cat: the 'safe zone' in the center is green, the
# middle 'warning' zone is yellow, and the periphery ('danger zone')
# is red. The game is to keep the cat alive by not
# letting it run off the edge of the screen.
#
# state -> event -> state
#from random import randint
#print (randint(-5,5))

def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if state[2] >= 0:
            newstate = randint(-5,-1)
        else:
            newstate = randint(1,5)
        if state[3] >= 0:
            newstate2 = randint(-5,-1)
        else:
            newstate2 = randint(1,5)
        return(state[0], state[1], newstate, newstate2, state[4], state[5])
    else:
        return(state)

################################################################

# The cat starts in the middle of the screen, moving diagonally
# towards the bottom right corner, with three lives
# initState = (x, y, dx, dy, lives, minutes, seconds)
initState = (width/2, height/2, 1, 1, 3, 0)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
