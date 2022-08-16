class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, p2):
        from math import sqrt
        if hasattr(p2, 'x') and hasattr(p2, 'y'):
            return sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)
        else:
            print('Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"