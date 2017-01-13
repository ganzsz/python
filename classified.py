#game met gebruik van classes
from ballclass import Ball
from paddleclass import Paddle

#import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

@window.event
def on_draw():
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    [draw_object[1].draw() for draw_object in object_list]

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

object_list = [("ball", Ball(100,200,50,50,4)),
               ("paddleR", Paddle(window.width-10,5,130,10)),
               ("paddleL", Paddle(0,5,130,10))]

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

pyglet.clock.schedule_interval(update, 0.005)
pyglet.app.run()