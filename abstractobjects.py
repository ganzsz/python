from pyglet.gl import *
from pyglet.window import *

class GameObject:

    def __init__(self, centerX, centerY, height, width, color):
        self.centerX = centerX
        self.centerY = centerY
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        raise Exception("you moron, you didnt make a draw method in", self.__class__.__name__)

class RectangleObject(GameObject):
    def __init__(self, centerX, centerY, height, width, color):
        super().__init__(centerX, centerY, height, width, color)

    def draw(self):
        colorR, colorG, colorB = self.color
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', ((self.centerX - (self.width/2)), (self.centerY - (self.height/2)),
                                                             (self.centerX - (self.width/2)), (self.centerY + (self.height/2)), 
                                                             (self.centerX + (self.width/2)), (self.centerY + (self.height/2)),
                                                             (self.centerX + (self.width/2)), (self.centerY - (self.height/2)))),
                                                            ('c3B', (colorR, colorG, colorB,
                                                             colorR, colorG, colorB, 
                                                             colorR, colorG, colorB, 
                                                             colorR, colorG, colorB)))

    def update(self):
        super().update()