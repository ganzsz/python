from pyglet.gl import *
from pyglet.window import *
from abstractobjects import RectangleObject

class MiddleLine(RectangleObject):
    speed = 0.15

    def __init__(self, window, color):
        super().__init__(window.width/2, window.height/2, window.height, 2, color)

    def update(self):
        pass