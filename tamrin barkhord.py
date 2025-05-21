class Shape:
    def __init__(self, color, size, direction, speed, position):
        pass

    def move(self):
        pass

    def collide(self):
        pass

    def die(self):
        pass

    def reflect(self):
        pass


class Triangle(Shape):
    def __init__(self):
        super().__init__(color, size, direction, speed, position)
        self.max_collisions = 3


class Square(Shape):
    def __init__(self):
        super().__init__(color, size, direction, speed, position)
        self.max_collisions = 4


class Rectangle(Shape):
    def __init__(self):
        super().__init__(color, size, direction, speed, position)
        self.max_collisions = 5


class Circle(Shape):
    def __init__(self):
        super().__init__(color, size, direction, speed, position)
        self.max_collisions = float('inf')
