import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        len_ = self.length()
        if len_ == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / len_, self.y / len_)

    def __eq__(self, other):
        return (isinstance(other, Vector2D) and
                self.x == other.x and self.y == other.y)