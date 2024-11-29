import unittest
from main.snake import Snake
from main.vector2d import Vector2D

class TestSnake(unittest.TestCase):

    def test_initial_length(self):
        snake = Snake(Vector2D(0, 0))
        self.assertEqual(len(snake.points), 1)

    def test_add_point_small_step(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(1, 2))
        self.assertEqual(len(snake.points), 4)

    def test_add_point_large_step(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(15, 5))
        self.assertEqual(len(snake.points), 21)

    def test_collision_handling_vertical(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(0, 3))
        snake.add_point(Vector2D(0, 0)) #collision
        self.assertEqual(len(snake.points), 4) #начальная точка + 3 точки

    def test_collision_handling_horizontal(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(3, 0))
        snake.add_point(Vector2D(0, 0))
        self.assertEqual(len(snake.points), 4)

    def test_collision_handling_diagonal(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(3, 4))
        snake.add_point(Vector2D(0, 0)) # collision
        self.assertEqual(len(snake.points), 14)

    def test_no_collisions_long(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(10, 5))
        snake.add_point(Vector2D(12, 7))
        snake.add_point(Vector2D(18, 13))
        snake.add_point(Vector2D(21, 6))
        self.assertEqual(len(snake.points), 42)

    def test_collisions_long(self):
        snake = Snake(Vector2D(2, 0))
        snake.add_point(Vector2D(4, 0))
        snake.add_point(Vector2D(4, 1))
        snake.add_point(Vector2D(3, 1))
        snake.add_point(Vector2D(3, -4))
        self.assertEqual(len(snake.points), 5)
