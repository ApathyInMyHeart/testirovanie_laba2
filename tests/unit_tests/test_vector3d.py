import unittest
import math
from main.vector3d import Vector3D


class TestVector3D(unittest.TestCase):

    def test_init(self):
        v = Vector3D(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_add(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v1 + v2, Vector3D(5, 7, 9))

    def test_sub(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v1 - v2, Vector3D(-3, -3, -3))

    def test_mul(self):
        v = Vector3D(1, 2, 3)
        scalar = 2
        self.assertEqual(v * scalar, Vector3D(2, 4, 6))

    def test_length(self):
        v = Vector3D(3, 4, 5)
        self.assertAlmostEqual(v.length(), 7.07106781, places=5)

    def test_normalize(self):
        v = Vector3D(3, 4, 5)
        normalized_v = v.normalize()
        self.assertAlmostEqual(normalized_v.length(), 1.0)
        self.assertAlmostEqual(normalized_v.x, 0.42426406, places=5)
        self.assertAlmostEqual(normalized_v.y, 0.56568542, places=5)
        self.assertAlmostEqual(normalized_v.z, 0.70710678, places=5)

    def test_dot_product(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v1.dot_product(v2), 32)

    def test_cross_product(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        cross_product = v1.cross_product(v2)
        self.assertEqual(cross_product, Vector3D(-3, 6, -3))

    def test_scalar_triple_product(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        v3 = Vector3D(7, 8, 9)
        stp = v1.scalar_triple_product(v2, v3)
        self.assertEqual(stp, 0)  # Векторы компланарны