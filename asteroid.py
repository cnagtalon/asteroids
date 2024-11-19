import pygame
import random
from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        self.kill()
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle) * 1.2
        new_vector2 = self.velocity.rotate(-random_angle) * 1.2

        smaller_asteroid = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroid)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroid)

        new_asteroid1.velocity = new_vector1
        new_asteroid2.velocity = new_vector2