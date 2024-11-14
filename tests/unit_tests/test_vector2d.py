import unittest
import math
from main.vector2d import Vector2D


class TestVector2D(unittest.TestCase):

    def test_init(self):
        v = Vector2D(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_add(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        self.assertEqual(v1 + v2, Vector2D(4, 6))

    def test_sub(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        self.assertEqual(v1 - v2, Vector2D(-2, -2))

    def test_mul(self):
        v = Vector2D(1, 2)
        scalar = 3
        self.assertEqual(v * scalar, Vector2D(3, 6))

    def test_length(self):
        v = Vector2D(3, 4)
        self.assertAlmostEqual(v.length(), 5.0, places=5)

    def test_normalize(self):
        v = Vector2D(3, 4)
        normalized_v = v.normalize()
        self.assertAlmostEqual(normalized_v.length(), 1.0)
        self.assertAlmostEqual(normalized_v.x, 0.6, places=5)
        self.assertAlmostEqual(normalized_v.y, 0.8, places=5)

    def test_zero_vector(self):
        v = Vector2D(0, 0)
        self.assertEqual(v.normalize(), Vector2D(0, 0))  # Проверка нормализации нулевого вектора