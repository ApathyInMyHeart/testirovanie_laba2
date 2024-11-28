# main/snake3d.py
import random
from main.vector3d import Vector3D

class Snake3D:
    def __init__(self, start_point: Vector3D):
        self.points = [start_point]
        self.directions = [(0, 0, 1), (1, 0, 0), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (0, -1, 0)] #вдоль осей координат
        self.current_direction = random.choice(self.directions)

    def add_point(self, target_point: Vector3D):
        last_point = self.points[-1]
        dx = target_point.x - last_point.x
        dy = target_point.y - last_point.y
        dz = target_point.z - last_point.z

        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0
        step_z = 1 if dz > 0 else -1 if dz < 0 else 0

        abs_dx, abs_dy, abs_dz = abs(dx), abs(dy), abs(dz)

        while abs_dx > 0 or abs_dy > 0 or abs_dz > 0:
            if abs_dx > 0:  # Двигаемся по X
                new_point = Vector3D(last_point.x + step_x, last_point.y, last_point.z)
                abs_dx -= 1
            elif abs_dy > 0:  # Двигаемся по Y
                new_point = Vector3D(last_point.x, last_point.y + step_y, last_point.z)
                abs_dy -= 1
            elif abs_dz > 0:  # Двигаемся по Z
                new_point = Vector3D(last_point.x, last_point.y, last_point.z + step_z)
                abs_dz -= 1
            else:
                break

            if self._is_collision(new_point):  # Проверяем столкновение
                return

            self.points.append(new_point)  # Записываем новую точку
            last_point = new_point  # Обновляем последнюю точку

    def _is_collision(self, new_point: Vector3D):
        for point in self.points[:-1]: #Исключаем последнюю точку из проверки
            if point == new_point:
                return True
        return False

    def __repr__(self):
        return f"Snake3D({self.points})"