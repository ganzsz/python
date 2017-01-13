#voorbeeld van gebruik met de kale ball class
import sys, time, math, os, random
from pyglet.gl import *

window = pyglet.window.Window()
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)


class ball:
    def __init__(self, x, y, Xsize, Ysize):
        self.x=x
        self.y=y
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.dy = 2
        self.dx = 2

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            [self.x, self.y, self.x-self.Xsize, self.y, self.x-self.Xsize, self.y-self.Ysize, self.x, self.y-self.Ysize]))

    def update(self):
        global window
        if(self.x==window.width):
            self.dx=-2
        if(self.x==self.Xsize):
            self.dx=2
        if(self.y==window.height):
            self.dy=-2
        if(self.y==self.Ysize):
            self.dy=2
        self.y+=self.dy
        self.x+=self.dx


@window.event
def on_draw():
    global ball
    glClearColor(0, 0.2, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    ball.draw()

def update(tm):
    global ball
    ball.update()
    
@window.event
def on_key_press(symbol, modifiers):
    global ball
    ball.update()
ball=ball(100,200,50,50)


pyglet.clock.schedule_interval(update, 0.005)
pyglet.app.run()