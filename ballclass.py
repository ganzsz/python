from pyglet.gl import *
from pyglet.window import *
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

    def update(self, window, paddleR, paddleL):
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
            print('paddle right')
        if(self.x-self.Xsize<=paddleL.left+paddleL.width 
                                and ((self.y<paddleL.position+(paddleL.height/2) and self.y>paddleL.position-(paddleL.height/2)) 
                                  or (self.y<paddleL.position+self.Ysize+(paddleL.height/2) and self.y>paddleL.position+self.Ysize-(paddleL.height/2)))):
            self.dx=self.speed
            print('paddle left')

        self.y+=self.dy
        self.x+=self.dx
