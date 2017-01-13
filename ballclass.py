#class voor bal om te importeren
from paddleclass import Paddle

from pyglet.gl import *
from pyglet.window import *

class Ball:
    def __init__(self, x, y, width, height, speed):
        self.x=x
        self.y=y
        self.width = width
        self.height = height
        self.speed = speed
        self.dy = speed
        self.dx = speed

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            [self.x, self.y, self.x-self.width, self.y, self.x-self.width, self.y-self.height, self.x, self.y-self.height]))


    def update(self, window, paddleRight, paddleLeft):
        if self.x>=paddleRight.left:
            if (paddleRight.position-(paddleRight.height/2) <= self.y <= (paddleRight.position+(paddleRight.height/2)) or (paddleRight.position-(paddleRight.height/2) <= self.y-self.height <= paddleRight.position+(paddleRight.height/2))):
                self.speed += 2
                Paddle.speed += 0.4
                self.dx=-self.speed
                print('paddle right')
        elif self.x-self.width<=paddleLeft.left+paddleLeft.width:
            if((self.y<paddleLeft.position+(paddleLeft.height/2) and self.y>paddleLeft.position-(paddleLeft.height/2)) or (self.y<paddleLeft.position+self.height+(paddleLeft.height/2) and self.y>paddleLeft.position+self.height-(paddleLeft.height/2))):
                self.speed += 2
                Paddle.speed += 0.4
                self.dx=self.speed
                print('paddle left')
        if(self.x>=window.width):
            self.dx=-self.speed
            print('right')
        elif(self.x<=self.width):
            self.dx=self.speed
            print('left')

        if(self.y>=window.height):
            self.dy=-self.speed
            print('top')
        elif(self.y<=self.height):
            self.dy=self.speed
            print('bot')

        self.y+=self.dy
        self.x+=self.dx
