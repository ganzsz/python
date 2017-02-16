from abstractobjects import RectangleObject

class Paddle(RectangleObject):
    speed = 0.15

    def reset(self):
        self.speed = 0.15

    def moveUp(self, window, deltaTime):
        if((self.centerY + (self.height/2)) <= (window.height - self.speed)):
            self.centerY += self.speed * deltaTime
        elif((window.height - self.speed) < (self.centerY + (self.height/2)) < window.height):
            self.centerY = window.height - (self.height/2)

    def moveDown(self, window, deltaTime):
        if(self.centerY - (self.height/2) >= self.speed):
            self.centerY -= self.speed * deltaTime
        elif(0 < (self.centerY - (self.height/2)) < self.speed):
            self.centerY = self.height/2

    def update(self):
        pass