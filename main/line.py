import math
from main.vector2d import Vector2D

class Line2D:
    def __init__(self, point1: Vector2D, point2: Vector2D):
        self.point1 = point1
        self.point2 = point2

    def distance_to_point(self, point: Vector2D):
        x0, y0 = point.x, point.y
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y

        return abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def is_parallel(self, other):
        dx1 = self.point2.x - self.point1.x
        dy1 = self.point2.y - self.point1.y
        dx2 = other.point2.x - other.point1.x
        dy2 = other.point2.y - other.point1.y

        return abs(dx1 * dy2 - dx2 * dy1) < 1e-6

    def intersection(self, other):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        x3, y3 = other.point1.x, other.point1.y
        x4, y4 = other.point2.x, other.point2.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if abs(denominator) < 1e-6: # учитываем погрешность
            return None  # Линии параллельны или совпадают

        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
        return Vector2D(x, y)


    def point_on_line(self, point: Vector2D):
        # Проверка, лежит ли точка на линии.  Учитываем погрешность.
        v1 = point - self.point1
        v2 = self.point2 - self.point1
        cross_product = v1.x * v2.y - v1.y * v2.x
        return abs(cross_product) < 1e-6

    def angle(self, other):
        v1 = self.point2 - self.point1
        v2 = other.point2 - other.point1
        dot_product = v1.x * v2.x + v1.y * v2.y
        len1 = v1.length()
        len2 = v2.length()
        if len1 == 0 or len2 == 0:
            return 0  # Или другое значение по умолчанию, если длина вектора 0
        return math.acos(dot_product / (len1 * len2))