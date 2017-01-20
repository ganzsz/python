#class voor bal om te importeren
from paddleclass import Paddle
from gameobjectclass import GameObject

from pyglet.gl import *
from pyglet.window import *

class Ball(GameObject):
    speed = 4
    def __init__(self, centerX, centerY, height, width):
        super().__init__(centerX, centerY, height, width)
        self.dy = self.speed
        self.dx = self.speed

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            ((self.centerX - (self.width/2)), (self.centerY - (self.height/2)),
             (self.centerX - (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY - (self.height/2)))))

    def update(self, window, paddleRight, paddleLeft):
        if(self.centerX + (self.width/2) >= paddleRight.centerX - (paddleRight.width/2)):
            if((paddleRight.centerY - paddleRight.height/2 <= self.centerY + self.height/2 <= paddleRight.centerY + paddleRight.height/2)
            or (paddleRight.centerY - paddleRight.height/2 <= self.centerY - self.height/2 <= paddleRight.centerY + paddleRight.height/2)):
                #self.speed += 0.5
                #Paddle.speed += 0.4
                self.dx=-self.speed
                print('paddle right')
        if(self.centerX - (self.width/2) <= paddleLeft.centerX + (paddleLeft.width/2)):
            if((paddleLeft.centerY - paddleLeft.height/2 <= self.centerY + self.height/2 <= paddleLeft.centerY + paddleLeft.height/2)
            or (paddleLeft.centerY - paddleLeft.height/2 <= self.centerY - self.height/2 <= paddleLeft.centerY + paddleLeft.height/2)):
                #self.speed += 0.5
                #Paddle.speed += 0.4
                self.dx=self.speed
                print('paddle left')
        if(self.centerX + self.width/2 >= window.width):
            self.dx=-self.speed
            print('right')
        elif(self.centerX - self.width/2 <= 0):
            self.dx=self.speed
            print('left')

        if(self.centerY + self.height/2 >= window.height):
            self.dy=-self.speed
            print('top')
        elif(self.centerY - self.height/2 <= 0):
            self.dy=self.speed
            print('bot')

        self.centerY+=self.dy
        self.centerX+=self.dx
