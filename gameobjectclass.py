class GameObject:

    def __init__(self, centerX, centerY, height, width):
        self.centerX = centerX
        self.centerY = centerY
        self.height = height
        self.width = width

    def draw(self):
        raise Exception("you moron, you didnt make a draw method in", self.__class__.__name__)