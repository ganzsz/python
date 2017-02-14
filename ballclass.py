#class voor bal om te importeren
from paddleclass import Paddle
from abstractobjects import RectangleObject

class Ball(RectangleObject):
    speed = 0.15 #TODO function for speed incremention for smoooooth criminal stuff
    ballIncrement = 0.025
    paddleIncrement = 0.02

    def __init__(self, centerX, centerY, height, width, color):
        super().__init__(centerX, centerY, height, width, color)
        self.dy = self.speed
        self.dx = self.speed


    def update(self, window, deltaTime, paddleRight, paddleLeft):
        if(self.centerX + (self.width/2) >= paddleRight.centerX - (paddleRight.width/2)):
            if((paddleRight.centerY - paddleRight.height/2 <= self.centerY + self.height/2 <= paddleRight.centerY + paddleRight.height/2)
            or (paddleRight.centerY - paddleRight.height/2 <= self.centerY - self.height/2 <= paddleRight.centerY + paddleRight.height/2)):
                self.speed += self.ballIncrement
                Paddle.speed += self.paddleIncrement
                self.dx=-self.speed
                print('paddle right')
        if(self.centerX - (self.width/2) <= paddleLeft.centerX + (paddleLeft.width/2)):
            if((paddleLeft.centerY - paddleLeft.height/2 <= self.centerY + self.height/2 <= paddleLeft.centerY + paddleLeft.height/2)
            or (paddleLeft.centerY - paddleLeft.height/2 <= self.centerY - self.height/2 <= paddleLeft.centerY + paddleLeft.height/2)):
                self.speed += self.ballIncrement
                Paddle.speed += self.paddleIncrement
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

        self.centerY+=self.dy * deltaTime
        self.centerX+=self.dx * deltaTime
