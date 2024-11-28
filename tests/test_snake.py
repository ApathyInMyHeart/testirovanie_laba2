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
        self.assertEqual(len(snake.points), 3)

    def test_add_point_large_step(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(5, 1))
        self.assertEqual(len(snake.points), 6)

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
        snake.add_point(Vector2D(3, 3))
        snake.add_point(Vector2D(0, 0)) # collision
        self.assertEqual(len(snake.points), 4)

    def test_no_collisions_long(self):
        snake = Snake(Vector2D(0, 0))
        snake.add_point(Vector2D(10, 0))
        snake.add_point(Vector2D(10, 10))
        snake.add_point(Vector2D(0, 10))
        snake.add_point(Vector2D(0, 0))
        self.assertEqual(len(snake.points), 40)

    def test_complex_scenario(self):
        snake = Snake(Vector2D(10, 10))
        points_to_add = [Vector2D(10, 20), Vector2D(20, 20), Vector2D(20, 10), Vector2D(10, 10)]
        for point in points_to_add:
            snake.add_point(point)
        self.assertGreater(len(snake.points), 1)
        for i in range(len(snake.points)):
            for j in range(i + 1, len(snake.points)):
                self.assertNotEqual(snake.points[i], snake.points[j])

    def test_no_collisions_complex(self):
        snake = Snake(Vector2D(0,0))
        points = [Vector2D(5,5), Vector2D(10,5), Vector2D(10,10),Vector2D(5,10),Vector2D(5,5)]
        for p in points:
            snake.add_point(p)
        self.assertEqual(len(snake.points), 25)
        for i in range(len(snake.points)):
          for j in range(i+1, len(snake.points)):
            self.assertNotEqual(snake.points[i], snake.points[j])