#link: http://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/programming_guide/quickstart.html

import pyglet
from pyglet.window import mouse, key

window = pyglet.window.Window(800, 600)

scoreLabel = pyglet.text.Label(text = 'Score: 0', x = 10, y = 575)
levelLabel = pyglet.text.Label(text = 'My amazing Game', x = 400, y = 575, anchor_x = 'center')

rectangleCounter = 'TL'
TLRectangleVar = (0, 0)
BRRectangleVar = (0, 0)

@window.event
def on_draw():
	window.clear()
	scoreLabel.draw()
	levelLabel.draw()
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
			('v2i', (10, 100, 10, 300, 210, 300, 210, 100)), 
			('c3B', ((0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0))))

@window.event
def on_key_press(symbol, modifiers):
	print('key', key.symbol_string(symbol),'is pressed')

@window.event
def on_mouse_press(x, y, button, modifiers):
	print('x =', x,'y =', y, 'left button' if button == mouse.LEFT else 'right button')
	if(button == mouse.LEFT):
		if(rectangleCounter == 'TL'):
			TLRectangleVar == (x, y)
			rectangleCounter == 'BR'
		elif(rectangleCounter == 'BR'):
			BRRectangleVar == (x, y)
			rectangleCounter == 'TL'
	if(TLRectangleVar != BRRectangleVar):
		pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (TLRectangleVar[0], TLRectangleVar[1], BRRectangleVar[0], BRRectangleVar[1])), ('c3B', (0, 255, 0)))

	
pyglet.app.run()