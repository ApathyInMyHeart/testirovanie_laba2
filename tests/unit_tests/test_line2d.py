import unittest
from main.vector2d import Vector2D
from main.line import Line2D
import math

class TestLine2D(unittest.TestCase):

    def test_init(self):
        p1 = Vector2D(1, 2)
        p2 = Vector2D(3, 4)
        line = Line2D(p1, p2)
        self.assertEqual(line.point1, p1)
        self.assertEqual(line.point2, p2)

    def test_distance_to_point(self):
        line = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        point = Vector2D(1, 0)
        distance = line.distance_to_point(point)
        self.assertAlmostEqual(distance, 0.70710678, places=5)  # Ожидаемое расстояние ≈ 0.707

    def test_is_parallel(self):
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        line2 = Line2D(Vector2D(1, 1), Vector2D(2, 2))
        self.assertTrue(line1.is_parallel(line2))

        line3 = Line2D(Vector2D(0, 0), Vector2D(1, 0))
        line4 = Line2D(Vector2D(0, 1), Vector2D(1, 2))
        self.assertFalse(line3.is_parallel(line4))

    def test_intersection(self):
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        line2 = Line2D(Vector2D(0, 1), Vector2D(1, 0))
        intersection = line1.intersection(line2)
        self.assertEqual(intersection, Vector2D(0.5, 0.5))

        # Проверка параллельных линий
        line3 = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        line4 = Line2D(Vector2D(0, 1), Vector2D(1, 2))
        self.assertIsNone(line3.intersection(line4))

    def test_point_on_line(self):
        line = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        point1 = Vector2D(0.5, 0.5)
        point2 = Vector2D(1.5, 1.5)

        self.assertTrue(line.point_on_line(point1))
        self.assertTrue(line.point_on_line(point2))
        self.assertFalse(line.point_on_line(Vector2D(1, 0)))

    def test_angle(self):
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 0))  # Горизонтальная линия
        line2 = Line2D(Vector2D(0, 0), Vector2D(1, 1))  # Линия под углом 45 градусов
        angle = line1.angle(line2)
        self.assertAlmostEqual(angle, math.pi / 4)

        line3 = Line2D(Vector2D(0, 0), Vector2D(1, 0))
        line4 = Line2D(Vector2D(0, 0), Vector2D(-1, 0))  # Линия под углом 180 градусов
        angle2 = line3.angle(line4)
        self.assertAlmostEqual(angle2, math.pi)