#game met gebruik van classes
from ballclass import Ball
from paddleclass import Paddle
from middlelineclass import MiddleLine
from textboxclass import *
from abstractobjects import RectangleObject

#import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *
import time
import random

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

@window.event
def on_draw():
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    if(gameStarted == False):
        startMessage = TextBox(window.width/2, window.height/2, 2, 2, (0, 0, 0))
        startMessage.text = "Press spacebar to start"
        startMessage.draw()
    else:
        global gameStarting
        #[draw_object[1].draw() for draw_object in object_list] cant be used to to order of drawing
        objectCounter = len(object_list)
        while objectCounter > 0:
            objectCounter -= 1
            object_list[objectCounter][1].draw()







current_milli_time = lambda: int(round(time.time() * 1000))

gameStarted = False
gameStarting = 3

oldTime = 0 #placeholder value
newTime = 0 #placeholder value

def update(timePassed):
    global newTime
    global oldTime
    global gameStarted
    oldTime = newTime
    newTime = current_milli_time()
    deltaTime = newTime - oldTime
    print(deltaTime)
    if(up==True):
        paddle_list[0].moveUp(window, deltaTime)
    if(down==True):
        paddle_list[0].moveDown(window, deltaTime)
    if(sKey==True):
        paddle_list[1].moveDown(window, deltaTime)
    if(wKey==True):
        paddle_list[1].moveUp(window, deltaTime)

    if(object_list[0][1].update(window, deltaTime, paddle_list[0], paddle_list[1],object_list[3][1])):
        object_list[0][1].reset(window)
        object_list[1][1].reset()
        object_list[2][1].reset()
        gameStarted = False
        pyglet.clock.unschedule(update)


object_list = [("ball", Ball((window.width/2), (window.height/2), 20, 20, (0, 255, 0))),
               ("paddleR", Paddle(window.width-5, (window.height/2), 100, 10, (255, 0, 0))),
               ("paddleL", Paddle(5, (window.height/2), 100, 10, (255, 0, 0))),
               ("counter", Score(window, (0, 0, 0))),
               ("middleLine", MiddleLine(window, (0, 0, 255)))]

paddle_list = [object_list[1][1], object_list[2][1]]
    



up = False
down = False
wKey = False
sKey = False

@window.event
def on_key_press(symbol, modifiers):
    global up
    global down
    global wKey
    global sKey
    global gameStarted
    if (symbol == key.UP):
        up = True
    if(symbol == key.DOWN):
        down = True
    if(symbol == key.W):
        wKey = True
    if(symbol == key.S):
        sKey = True
    if(symbol == key.SPACE):
        gameStarted = True
        global newTime
        newTime = current_milli_time()
        pyglet.clock.schedule_interval(update, 1/60.0)
        if(random.random() <= 0.5):
            object_list[0][1].setDx(-1)
        if(random.random() <= 0.5):
            object_list[0][1].setDy(-1)


@window.event
def on_key_release(symbol, modifiers):
    if(symbol==key.UP):
        global up
        up = False
    if(symbol==key.DOWN):
        global down
        down = False
    if(symbol==key.W):
        global wKey
        wKey = False
    if(symbol==key.S):
        global sKey
        sKey = False

pyglet.app.run()