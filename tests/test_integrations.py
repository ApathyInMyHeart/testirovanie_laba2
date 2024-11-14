import math
import unittest
from main.vector3d import Vector3D
from main.vector2d import Vector2D
from main.line import Line2D
from main.plane3d import Plane3D


class TestIntegrations(unittest.TestCase):

    def test_line2d_with_vector2d(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        line = Line2D(v1, v2)
        v3 = Vector2D(2, 3)  # Точка на линии
        v4 = Vector2D(0, 0)   # Точка вне линии

        self.assertAlmostEqual(line.distance_to_point(v3), 0.0) # расстояние до точки на линии = 0
        self.assertGreater(line.distance_to_point(v4), 0.0) # расстояние до точки вне линии > 0

    def test_plane3d_with_vector3d(self):
        point = Vector3D(1, 1, 1)
        normal = Vector3D(0, 0, 1)
        plane = Plane3D(point, normal)
        point_on_plane = Vector3D(2, 2, 1)
        point_off_plane = Vector3D(2, 2, 2)

        self.assertAlmostEqual(plane.distance_to_point(point_on_plane), 0.0)
        self.assertGreater(plane.distance_to_point(point_off_plane), 0.0)

    def test_line2d_intersection_with_vector2d(self):
        line1 = Line2D(Vector2D(0, 0), Vector2D(2, 2))
        line2 = Line2D(Vector2D(0, 2), Vector2D(2, 0))
        intersection = line1.intersection(line2)

        self.assertEqual(intersection, Vector2D(1, 1)) # проверяем координаты точки пересечения

        line3 = Line2D(Vector2D(0, 0), Vector2D(1, 1)) # параллельные линии
        line4 = Line2D(Vector2D(0, 1), Vector2D(1, 2))
        self.assertIsNone(line3.intersection(line4))


    def test_plane3d_intersection_with_vector3d_line(self):
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        p1 = Vector3D(0, 0, 10)
        p2 = Vector3D(1, 1, -10)
        intersection = plane.intersection_with_line(p1, p2)
        self.assertAlmostEqual(intersection.x, 0.5)
        self.assertAlmostEqual(intersection.y, 0.5)
        self.assertAlmostEqual(intersection.z, 0.0)

    def test_line2d_distance_to_point(self):
        line = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        point = Vector2D(1, 0)
        distance = line.distance_to_point(point)
        self.assertAlmostEqual(distance, 0.70710678, places=5)  # Ожидаемое расстояние ≈ 0.707

    def test_line2d_angle_between_lines(self):  # Добавьте этот тест, если реализовали метод angle в Line2D
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 0))  # Горизонтальная линия
        line2 = Line2D(Vector2D(0, 0), Vector2D(1, 1))  # Линия под углом 45 градусов
        angle = line1.angle(line2)  # Предполагается, что метод angle возвращает угол в радианах
        self.assertAlmostEqual(angle, math.pi / 4)

        line3 = Line2D(Vector2D(0, 0), Vector2D(1, 0))
        line4 = Line2D(Vector2D(0, 0), Vector2D(-1, 0))  # Линия под углом 180 градусов
        angle2 = line3.angle(line4)
        self.assertAlmostEqual(angle2, math.pi)

    def test_point_on_plane3d(self):
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        point_on_plane = Vector3D(1, 2, 0)
        point_off_plane = Vector3D(1, 2, 1)

        # Если реализован метод point_on_plane в Plane3D:
        self.assertTrue(plane.point_on_plane(point_on_plane))
        self.assertFalse(plane.point_on_plane(point_off_plane))

        # Если нет метода point_on_plane, можно проверить расстояние:
        self.assertAlmostEqual(plane.distance_to_point(point_on_plane), 0)
        self.assertNotAlmostEqual(plane.distance_to_point(point_off_plane), 0)

    # Добавьте другие интеграционные тесты