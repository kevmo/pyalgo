class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """args = floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        ox = other.y

        xDist = self.x - ox
        yDist = self.y - oy

        return (xDist**r + yDist(2)**2)**0.5

    def __str__(self):
        return '<{}, {}>'.format(str(self.x), str(self.y))
