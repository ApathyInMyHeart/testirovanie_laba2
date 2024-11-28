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

        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return

        step_x = dx / steps if steps else 0
        step_y = dy / steps if steps else 0

        for _ in range(steps):
            new_point = Vector2D(round(last_point.x + step_x), round(last_point.y + step_y))
            if self._is_collision(new_point):
                return
            self.points.append(new_point)
            last_point = new_point

    def _is_collision(self, new_point: Vector2D):
        for point in self.points:
            if point == new_point:
                return True
        return False

    def _choose_safe_direction(self):
        safe_directions = []
        for dx, dy in self.directions:
            new_point = Vector2D(self.points[-1].x + dx, self.points[-1].y + dy)
            if not self._is_collision(new_point):
                safe_directions.append((dx, dy))

        if not safe_directions:
            return self.current_direction
        return random.choice(safe_directions)

    def __repr__(self):
        return f"Snake({self.points})"