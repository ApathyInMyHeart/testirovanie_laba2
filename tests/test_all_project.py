import math
import unittest
from main.vector3d import Vector3D
from main.vector2d import Vector2D
from main.line import Line2D
from main.plane3d import Plane3D


class TestAllProject(unittest.TestCase):

    def test_3d_intersection(self):
        # Создаем плоскость и линию в 3D
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        line_point1 = Vector3D(0, 0, 10)
        line_point2 = Vector3D(1, 1, -10)

        # Находим точку пересечения
        intersection = plane.intersection_with_line(line_point1, line_point2)

        # Проверяем, что точка пересечения лежит на плоскости
        self.assertAlmostEqual(plane.distance_to_point(intersection), 0.0)

    def test_2d_intersection(self):
        # Создаем две линии в 2D
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        line2 = Line2D(Vector2D(0, 1), Vector2D(1, 0))

        # Находим точку пересечения
        intersection = line1.intersection(line2)

        # Проверяем координаты точки пересечения
        self.assertAlmostEqual(intersection.x, 0.5)
        self.assertAlmostEqual(intersection.y, 0.5)


    def test_parallel_lines(self):
        # Создаем две параллельные линии
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        line2 = Line2D(Vector2D(1, 1), Vector2D(2, 2))

        # Проверяем, что они параллельны
        self.assertTrue(line1.is_parallel(line2))

        # Проверяем, что точка пересечения отсутствует
        self.assertIsNone(line1.intersection(line2))

    def test_perpendicular_planes(self):
      plane1 = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
      plane2 = Plane3D(Vector3D(0, 0, 0), Vector3D(1, 0, 0))

      self.assertTrue(plane1.is_perpendicular(plane2))
      self.assertFalse(plane1.is_parallel(plane2))

    def test_vector3d_operations(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        scalar = 2

        self.assertEqual(v1 + v2, Vector3D(5, 7, 9))
        self.assertEqual(v1 - v2, Vector3D(-3, -3, -3))
        self.assertEqual(v1 * scalar, Vector3D(2, 4, 6))
        self.assertAlmostEqual(v1.length(), 3.741657, places=5)
        self.assertEqual(v1.dot_product(v2), 32)

        normalized_v1 = v1.normalize()
        self.assertAlmostEqual(normalized_v1.length(), 1.0, places=5)

        cross_product = v1.cross_product(v2)
        self.assertEqual(cross_product, Vector3D(-3, 6, -3))

        v3 = Vector3D(7, 8, 9)
        stp = v1.scalar_triple_product(v2, v3)
        self.assertEqual(stp, 0) # В данном случае векторы компланарны, поэтому смешанное произведение 0.


    def test_vector2d_operations(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        scalar = 3

        self.assertEqual(v1 + v2, Vector2D(4, 6))
        self.assertEqual(v1 - v2, Vector2D(-2, -2))
        self.assertEqual(v1 * scalar, Vector2D(3, 6))
        self.assertAlmostEqual(v1.length(), 2.236067, places=5)


    def test_line2d_point_on_line(self):
        line = Line2D(Vector2D(0, 0), Vector2D(1, 1))
        point1 = Vector2D(0.5, 0.5)
        point2 = Vector2D(1.5, 1.5)

        self.assertTrue(line.point_on_line(point1))  # Точка лежит на линии
        self.assertTrue(line.point_on_line(point2))
        self.assertFalse(line.point_on_line(Vector2D(1, 0))) # Точка не лежит на линии



    def test_plane3d_distance(self):
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        point = Vector3D(1, 2, 3)
        self.assertEqual(plane.distance_to_point(point), 3)

    def test_plane3d_parallel_perpendicular(self):
        plane1 = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        plane2 = Plane3D(Vector3D(1, 1, 1), Vector3D(0, 0, 1))  # Параллельная плоскость
        plane3 = Plane3D(Vector3D(0, 0, 0), Vector3D(1, 0, 0))  # Перпендикулярная плоскость

        self.assertTrue(plane1.is_parallel(plane2))
        self.assertTrue(plane1.is_perpendicular(plane3))

    def test_angle_between_lines_and_intersection(self):
        line1 = Line2D(Vector2D(0, 0), Vector2D(1, 0))
        line2 = Line2D(Vector2D(0, 0), Vector2D(0, 1))
        angle = line1.angle(line2)
        self.assertAlmostEqual(angle,
                               math.pi / 2)  # Угол между горизонтальной и вертикальной линией - 90 градусов (pi/2 радиан)

        intersection = line1.intersection(line2)
        self.assertEqual(intersection, Vector2D(0, 0))

    def test_point_on_plane_and_distance(self):
        plane = Plane3D(Vector3D(1, 2, 3), Vector3D(0, 0, 1))  # Плоскость параллельна XY
        point1 = Vector3D(4, 5, 3)  # Точка на плоскости
        point2 = Vector3D(4, 5, 4)  # Точка не на плоскости

        self.assertTrue(plane.point_on_plane(point1))
        self.assertFalse(plane.point_on_plane(point2))
        self.assertAlmostEqual(plane.distance_to_point(point1), 0)
        self.assertAlmostEqual(plane.distance_to_point(point2), 1.0)


if __name__ == '__main__':
  unittest.main()