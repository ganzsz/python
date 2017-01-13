#voorbeeld met classes en alles in een bestand
import sys, time, math, os, random
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

class game:
    def __init__(self):
        global window
        self.ball = ball(100,200,50,50,4)
        self.paddleR=paddle(window.width-10,5,130,10)
        self.paddleL=paddle(0,5,130,10)

    def keypress(self, symbol, modifiers):
        pass

    def keyrelease(self, symbol, modifiers):
        pass



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

class ball:
    def __init__(self, x, y, Xsize, Ysize, speed):
        self.x=x
        self.y=y
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.speed = speed
        self.dy = speed
        self.dx = speed

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            [self.x, self.y, self.x-self.Xsize, self.y, self.x-self.Xsize, self.y-self.Ysize, self.x, self.y-self.Ysize]))

    def update(self):
        global window
        global paddleR
        global paddleL
        if(self.x>=window.width):
            self.dx=-self.speed
            print('right')
        if(self.x<=self.Xsize):
            self.dx=self.speed
            print('left')
        if(self.y>=window.height):
            self.dy=-self.speed
            print('top')
        if(self.y<=self.Ysize):
            self.dy=self.speed
            print('bot')

        if(self.x>=paddleR.left and ((self.y<paddleR.position+(paddleR.height/2) and self.y>paddleR.position-(paddleR.height/2)) 
                                  or (self.y<paddleR.position+self.Ysize+(paddleR.height/2) and self.y>paddleR.position+self.Ysize-(paddleR.height/2)))):
            self.dx=-self.speed
        if(self.x-self.Xsize<=paddleL.left+paddleL.width 
                                and ((self.y<paddleL.position+(paddleL.height/2) and self.y>paddleL.position-(paddleL.height/2)) 
                                  or (self.y<paddleL.position+self.Ysize+(paddleL.height/2) and self.y>paddleL.position+self.Ysize-(paddleL.height/2)))):
            self.dx=self.speed
        self.y+=self.dy
        self.x+=self.dx

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
        paddleR.moveUp()
    if(down==1):
        paddleR.moveDown()
    if(sKey==1):
        paddleL.moveDown()
    if(wKey==1):
        paddleL.moveUp()

    global ball
    ball.update()

    
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