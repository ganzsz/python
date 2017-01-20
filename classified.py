#game met gebruik van classes
from ballclass import Ball
from paddleclass import Paddle

#import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *
import time

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

@window.event
def on_draw():
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    [draw_object[1].draw() for draw_object in object_list]

current_milli_time = lambda: int(round(time.time() * 1000))

def update(timePassed):
    if(up==True):
        paddle_list[0].moveUp(window)
    if(down==True):
        paddle_list[0].moveDown(window)
    if(sKey==True):
        paddle_list[1].moveDown(window)
    if(wKey==True):
        paddle_list[1].moveUp(window)

    object_list[0][1].update(window, paddle_list[0], paddle_list[1])

object_list = [("ball", Ball((window.width/2), (window.height/2), 40, 40)),
               ("paddleR", Paddle(window.width-5, (window.height/2), 120, 10)),
               ("paddleL", Paddle(5, (window.height/2), 120, 10))]

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
    if (symbol == key.UP):
        up = True
    if(symbol == key.DOWN):
        down = True
    if(symbol == key.W):
        wKey = True
    if(symbol == key.S):
        sKey = True

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

oldTime = current_milli_time

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()