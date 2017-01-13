#paddle met een class voorbeeld
import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

class paddle:
    def __init__(self, left, speed, height, width):
        self.position=150
        self.height = height
        self.width = width
        self.speed = speed
        self.left=left

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            [self.left, (self.position-(self.height/2)),
             self.left+self.width, (self.position+(self.height/2)),
             self.left+self.width, (self.position-(self.height/2)),
             self.left, (self.position+(self.height/2))]))

    def moveUp(self):
        if((self.position+(self.height/2))<window.height):
            self.position+=self.speed

    def moveDown(self):
        global window
        if(self.position>(self.height/2)):
            self.position-=self.speed

    def update(self):
        pass


@window.event
def on_draw():
    global paddleR
    global paddleL
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    paddleR.draw()
    paddleL.draw()

def update(tm):
    global paddleR
    global up
    global down
    global sKey
    global wKey
    if(up==1):
        paddleR.moveUp()
    if(down==1):
        paddleR.moveDown()
    if(sKey==1):
        paddleL.moveDown()
    if(wKey==1):
        paddleL.moveUp()

    
paddleR=paddle(window.width-10,5,80,10)
paddleL=paddle(0,5,80,10)


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