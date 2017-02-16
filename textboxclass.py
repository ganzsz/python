from abstractobjects import GameObject

from pyglet.gl import *
from pyglet.window import *

class TextBox(GameObject):
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

class Score(GameObject):
    def __init__(self, window, color):
        super().__init__(window.width/2, window.height/2, 2, 2, color)
        self.textOne = TextBox(window.width/2-100, window.height/2, 2, 2, color)
        self.textTwo = TextBox(window.width/2+100, window.height/2, 2, 2, color)
        self.textOne.text = 0
        self.textTwo.text = 0
        
    playerOne = 0
    playerTwo = 0
    def scorePlayerOne(self):
        self.playerOne+=1
        self.textOne.text=self.playerOne

    def scorePlayerTwo(self):
        self.playerTwo+=1
        self.textTwo.text = self.playerTwo

    def draw(self):
        self.textOne.draw()
        self.textTwo.draw()
