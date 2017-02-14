from gameobjectclass import GameObject

from pyglet.gl import *
from pyglet.window import *

class textBox(GameObject):
    text = "Hoi"
    def draw(self):
        pyglet.text.Label(self.text,
                          font_name='Comic Sans',
                          font_size=36,
                          x=self.centerX, y=self.centerY,
                          anchor_x='center', anchor_y='center').draw()

class score:
    playerOne = 0
    playerTwo = 0
    def scorePlayerOne(self):
        self.playerOne++

    def scorePlayerTwo(self):
        self.playerTwo++

