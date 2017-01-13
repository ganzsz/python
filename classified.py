#game met gebruik van classes
from ballclass import ball
from paddleclass import paddle

#import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

@window.event
def on_draw():
    global paddleR
    global paddleL
    global ball
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    paddleR.draw()
    paddleL.draw()
    ball.draw()

def update(timePassed):
    if(up==1):
        paddleR.moveUp(window)
    if(down==1):
        paddleR.moveDown(window)
    if(sKey==1):
        paddleL.moveDown(window)
    if(wKey==1):
        paddleL.moveUp(window)

    ball.update(window, paddleR, paddleL)

    
ball=ball(100,200,50,50,4)
paddleR=paddle(window.width-10,5,130,10)
paddleL=paddle(0,5,130,10)


up=0
down = 0
wKey = 0
sKey = 0
@window.event
def on_key_press(symbol, modifiers):
    global paddleR
    global up
    global down
    global wKey
    global sKey
    if (symbol == key.UP):
        up=1
    if(symbol==key.DOWN):
        down=1
    if(symbol==key.W):
        wKey=1
    if(symbol==key.S):
        sKey=1

@window.event
def on_key_release(symbol, modifiers):
    if(symbol==key.UP):
        global up
        up = 0
    if(symbol==key.DOWN):
        global down
        down=0
    if(symbol==key.W):
        global wKey
        wKey=0
    if(symbol==key.S):
        global sKey
        sKey=0

pyglet.clock.schedule_interval(update, 0.005)
pyglet.app.run()