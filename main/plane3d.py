from main.vector3d import Vector3D

class Plane3D:
    def __init__(self, point: Vector3D, normal: Vector3D):
        self.point = point
        self.normal = normal.normalize()

    def distance_to_point(self, point: Vector3D):
        return abs(self.normal.dot_product(point - self.point))


    def is_parallel(self, other):
        return abs(self.normal.dot_product(other.normal)) == 1

    def is_perpendicular(self, other):
        return self.normal.dot_product(other.normal) == 0

    def intersection_with_line(self, point1: Vector3D, point2: Vector3D):
        line_vector = point2 - point1
        denominator = self.normal.dot_product(line_vector)

        if abs(denominator) < 1e-6:  # Проверка на параллельность прямой и плоскости
            return None

        t = self.normal.dot_product(self.point - point1) / denominator
        intersection_point = point1 + line_vector * t


        return intersection_point

    def point_on_plane(self, point: Vector3D):
        return abs(self.distance_to_point(point)) < 1e-6