import random
from main.vector2d import Vector2D

class Snake:
    def __init__(self, start_point: Vector2D):
        self.points = [start_point]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.current_direction = random.choice(self.directions)

    def add_point(self, target_point: Vector2D):
        last_point = self.points[-1]
        dx = target_point.x - last_point.x
        dy = target_point.y - last_point.y

        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0

        abs_dx, abs_dy = abs(dx), abs(dy)

        while abs_dx > 0 or abs_dy > 0:
            if abs_dx > 0:  # Движение по X
                new_point = Vector2D(last_point.x + step_x, last_point.y)
                abs_dx -= 1
            elif abs_dy > 0:  # Движение по Y
                new_point = Vector2D(last_point.x, last_point.y + step_y)
                abs_dy -= 1
            else:
                break

            if self._is_collision(new_point):  # Проверка на столкновение
                return

            self.points.append(new_point)  # Запись новой точки
            last_point = new_point  # Обновление текущей точки

    def _is_collision(self, new_point: Vector2D):
        for point in self.points:
            if point == new_point:
                return True
        return False

    def __repr__(self):
        return f"Snake({self.points})"