#Kale class van de paddle om te importeren
from pyglet.gl import *
from pyglet.window import *
class Paddle:
    speed = 4

    def __init__(self, left, speed, height, width):
        self.position=150
        self.height = height
        self.width = width
        self.left=left

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            (self.left, (self.position-(self.height/2)),
             self.left, (self.position+(self.height/2)),
             self.left+self.width, (self.position+(self.height/2)),
             self.left+self.width, (self.position-self.height/2))))

    def moveUp(self, window):
        if((self.position+(self.height/2))<window.height):
            self.position+=self.speed

    def moveDown(self, window):
        if(self.position>(self.height/2)):
            self.position-=self.speed

    def update(self):
        pass