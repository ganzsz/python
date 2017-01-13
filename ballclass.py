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

    def update(self, window, paddleLeft, paddleRight):
        if(self.x>=window.width):
            self.dx=-self.speed
            print('right')
        if(self.x<=self.width):
            self.dx=self.speed
            print('left')
        if(self.y>=window.height):
            self.dy=-self.speed
            print('top')
        if(self.y<=self.height):
            self.dy=self.speed
            print('bot')

        if paddleLeft.left + paddleLeft.width < self.x - self.width:
            if paddleLeft.left + paddleLeft.width >= self.x - self.width + self.dx and (self.y - self.height <= paddleLeft.position + paddleLeft.height/2 <= self.y or self.y <= paddleLeft.position - paddleLeft.height/2 <= self.y - self.height):
                self.dx *= -1
                self.speed += .5
                paddle.speed += .4
                print('paddle left hit')
        if paddleRight.left > self.x:
            if paddleRight.left <= self.x + self.dx and (self.y - self.height <= paddleRight.position + paddleRight.height/2 <= self.y or self.y <= paddleRight.position - paddleRight.height/2 <= self.y - self.height):
                self.dx *= -1
                self.speed += .5
                paddle.speed += .4
                print('paddle right hit')

        self.y+=self.dy
        self.x+=self.dx
