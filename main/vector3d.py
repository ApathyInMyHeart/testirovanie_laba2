import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        len_ = self.length()
        if len_ == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / len_, self.y / len_, self.z / len_)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def scalar_triple_product(self, other1, other2):
        return self.dot_product(other1.cross_product(other2))

    def __eq__(self, other):
        return (isinstance(other, Vector3D) and
                self.x == other.x and self.y == other.y and self.z == other.z)

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"