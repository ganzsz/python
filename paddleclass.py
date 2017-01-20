#Kale class van de paddle om te importeren
from pyglet.gl import *
from pyglet.window import *
from gameobjectclass import GameObject

class Paddle(GameObject):
    speed = 100

    def __init__(self, centerX, centerY, height, width):
        super().__init__(centerX, centerY, height, width)

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            ((self.centerX - (self.width/2)), (self.centerY - (self.height/2)),
             (self.centerX - (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY - (self.height/2)))))

    def moveUp(self, window):
        if((self.centerY + (self.height/2)) <= (window.height - self.speed)):
            self.centerY += self.speed
        elif((window.height - self.speed) < (self.centerY + (self.height/2)) < window.height):
            self.centerY = window.height - (self.height/2)

    def moveDown(self, window):
        if(self.centerY - (self.height/2) >= self.speed):
            self.centerY -= self.speed
        elif(0 < (self.centerY - (self.height/2)) < self.speed):
            self.centerY = self.height/2

    def update(self):
        pass