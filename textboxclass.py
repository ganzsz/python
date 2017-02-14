from abstractobjects import GameObject

from pyglet.gl import *
from pyglet.window import *

class textBox(GameObject):
    text = "Hoi"
    def draw(self):
        pyglet.text.Label(str(self.text),
                          font_name='Comic Sans',
                          font_size=36,
                          x=self.centerX, y=self.centerY,
                          anchor_x='center', anchor_y='center').draw()

    def setText(self, text):
        self.text = text
        print(text)

class score(GameObject):
    def __init__(self, centerX, centerY, height, width):
        super().__init__(centerX, centerY, height, width)
        self.textOne = textBox(self.centerX-100, self.centerY, self.height, self.width)
        self.textTwo = textBox(self.centerX+100, self.centerY, self.height, self.width)
        self.textOne.text = 0
    playerOne = 0
    playerTwo = 0
    def scorePlayerOne(self):
        self.playerOne+=1
        self.textOne=self.playerOne

    def scorePlayerTwo(self):
        self.playerTwo+=1
        self.textTwo.text = self.playerTwo

    def draw(self):
        self.textOne.draw()
        self.textTwo.draw()
