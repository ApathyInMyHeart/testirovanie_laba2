import unittest
from main.snake3d import Snake3D
from main.vector3d import Vector3D

class TestSnake3D(unittest.TestCase):

    def test_initial_length(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        self.assertEqual(len(snake.points), 1)

    def test_add_point_small_step(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(1, 2, 0))
        self.assertEqual(len(snake.points), 4) # начальная + 3

    def test_add_point_large_step(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(5, 1, 2))
        self.assertEqual(len(snake.points), 9) # начальная + 8

    def test_collision_handling_x(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(3, 0, 0))
        snake.add_point(Vector3D(0, 0, 0))  # collision
        self.assertEqual(len(snake.points), 4)  # начальная + 3

    def test_collision_handling_y(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(0, 3, 0))
        snake.add_point(Vector3D(0, 0, 0))  # collision
        self.assertEqual(len(snake.points), 4)  # начальная + 3

    def test_collision_handling_z(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(0, 0, 3))
        snake.add_point(Vector3D(0, 0, 0))  # collision
        self.assertEqual(len(snake.points), 4)  # начальная + 3

    def test_no_collisions_long(self):
        snake = Snake3D(Vector3D(0, 0, 0))
        snake.add_point(Vector3D(7, 5, 6))
        snake.add_point(Vector3D(9, 8, 3))
        snake.add_point(Vector3D(12, 4, 5))
        snake.add_point(Vector3D(6, 6, 12))
        snake.add_point(Vector3D(15, 11, 7))
        snake.add_point(Vector3D(13, 6, 9))
        self.assertEqual(len(snake.points), 79)

    def test_collisions_long(self):
        snake = Snake3D(Vector3D(0, 0, 5))
        print(f"Final snake length: {len(snake.points)}")
        snake.add_point(Vector3D(10, 10, 10))
        print(f"Final snake length: {len(snake.points)}")
        snake.add_point(Vector3D(10, 5, 10))
        print(f"Final snake length: {len(snake.points)}")
        snake.add_point(Vector3D(10, 5, 0))
        print(f"Final snake length: {len(snake.points)}")
        self.assertEqual(len(snake.points), 35)
