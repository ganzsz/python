from pyglet.gl import *
from pyglet.window import *

class GameObject:

    def __init__(self, centerX, centerY, height, width):
        self.centerX = centerX
        self.centerY = centerY
        self.height = height
        self.width = width

    def draw(self):
        raise Exception("you moron, you didnt make a draw method in", self.__class__.__name__)

class RectangleObject(GameObject):
    def __init__(self, centerX, centerY, height, width):
        super().__init__(centerX, centerY, height, width)

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', 
            ((self.centerX - (self.width/2)), (self.centerY - (self.height/2)),
             (self.centerX - (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY + (self.height/2)),
             (self.centerX + (self.width/2)), (self.centerY - (self.height/2)))))

    def update(self):
        super().update()