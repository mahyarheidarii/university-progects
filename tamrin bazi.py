import pygame
import random
import math

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

class Shape:
    def __init__(self, x, y, angle, color, size=20, max_hits=3):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.size = size
        self.speed = 3
        self.hit_count = 0
        self.max_hits = max_hits
        self.dead = False

    def move(self):
        if self.dead:
            return
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed
        self.check_wall_collision()

    def check_wall_collision(self):
        r = self.size
        if self.x - r <= 0:
            self.x = r
            self.angle = 180 - self.angle
        elif self.x + r >= WIDTH:
            self.x = WIDTH - r
            self.angle = 180 - self.angle
        if self.y - r <= 0:
            self.y = r
            self.angle = -self.angle
        elif self.y + r >= HEIGHT:
            self.y = HEIGHT - r
            self.angle = -self.angle
        self.angle %= 360

    def check_collision_with(self, other):
        if self.dead or other.dead:
            return
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.hypot(dx, dy)
        if distance < self.size + other.size:
            self.hit_count += 1
            other.hit_count += 1
            if self.hit_count >= self.max_hits:
                self.dead = True
            if other.hit_count >= other.max_hits:
                other.dead = True

    def draw(self, screen):
        pass

class Triangle(Shape):
    def __init__(self, x, y, angle, color):
        super().__init__(x, y, angle, color, size=20, max_hits=3)

    def draw(self, screen):
        if not self.dead:
            points = [
                (self.x, self.y - 25),
                (self.x - 20, self.y + 15),
                (self.x + 20, self.y + 15)
            ]
            pygame.draw.polygon(screen, self.color, points)

class Square(Shape):
    def __init__(self, x, y, angle, color):
        super().__init__(x, y, angle, color, size=20, max_hits=4)

    def draw(self, screen):
        if not self.dead:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x - self.size, self.y - self.size, 2*self.size, 2*self.size))

class Rectangle(Shape):
    def __init__(self, x, y, angle, color):
        super().__init__(x, y, angle, color, size=30, max_hits=5)

    def draw(self, screen):
        if not self.dead:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x - 30, self.y - 15, 60, 30))

class Circle(Shape):
    def __init__(self, x, y, angle, color):
        super().__init__(x, y, angle, color, size=20, max_hits=6)

    def draw(self, screen):
        if not self.dead:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Collision")
clock = pygame.time.Clock()

shapes = [
    Triangle(random.randint(50, 750), random.randint(50, 550), random.randint(0, 360), COLORS[0]),
    Square(random.randint(50, 750), random.randint(50, 550), random.randint(0, 360), COLORS[1]),
    Rectangle(random.randint(50, 750), random.randint(50, 550), random.randint(0, 360), COLORS[2]),
    Circle(random.randint(50, 750), random.randint(50, 550), random.randint(0, 360), COLORS[3])
]

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for shape in shapes:
        shape.move()

    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            shapes[i].check_collision_with(shapes[j])

    for shape in shapes:
        shape.draw(screen)

    pygame.display.flip()

pygame.quit()
