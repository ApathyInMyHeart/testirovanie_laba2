import unittest
from main.vector3d import Vector3D
from main.plane3d import Plane3D
import math

class TestPlane3D(unittest.TestCase):

    def test_init(self):
        point = Vector3D(1, 2, 3)
        normal = Vector3D(0, 0, 1)
        plane = Plane3D(point, normal)
        self.assertEqual(plane.point, point)
        self.assertEqual(plane.normal, Vector3D(0, 0, 1)) # Нормальный вектор должен быть нормализован

    def test_distance_to_point(self):
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        point = Vector3D(1, 2, 3)
        self.assertEqual(plane.distance_to_point(point), 3)

    def test_is_parallel(self):
        plane1 = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        plane2 = Plane3D(Vector3D(1, 1, 1), Vector3D(0, 0, 1))  # Параллельная плоскость
        self.assertTrue(plane1.is_parallel(plane2))

        plane3 = Plane3D(Vector3D(0, 0, 0), Vector3D(1, 0, 0))  # Непараллельная плоскость
        self.assertFalse(plane1.is_parallel(plane3))

    def test_is_perpendicular(self):
        plane1 = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        plane2 = Plane3D(Vector3D(1, 1, 1), Vector3D(1, 0, 0))  # Перпендикулярная плоскость
        self.assertTrue(plane1.is_perpendicular(plane2))

        plane3 = Plane3D(Vector3D(0, 0, 0), Vector3D(1, 1, 5))  # Неперпендикулярная плоскость
        self.assertFalse(plane1.is_perpendicular(plane3))

    def test_intersection_with_line(self):
        plane = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        p1 = Vector3D(0, 0, 10)
        p2 = Vector3D(1, 1, -10)
        intersection = plane.intersection_with_line(p1, p2)
        self.assertAlmostEqual(intersection.x, 0.5)
        self.assertAlmostEqual(intersection.y, 0.5)
        self.assertAlmostEqual(intersection.z, 0.0)

        # Проверка параллельности прямой и плоскости
        plane2 = Plane3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1))
        p3 = Vector3D(0, 0, 10)
        p4 = Vector3D(1, 1, 10)  # Прямая параллельна плоскости
        self.assertIsNone(plane2.intersection_with_line(p3, p4))

    def test_point_on_plane(self):
        plane = Plane3D(Vector3D(1, 2, 3), Vector3D(0, 0, 1)) # Плоскость параллельна XY
        point1 = Vector3D(4, 5, 3) # Точка на плоскости
        point2 = Vector3D(4, 5, 4)  # Точка не на плоскости

        self.assertTrue(plane.point_on_plane(point1))
        self.assertFalse(plane.point_on_plane(point2))