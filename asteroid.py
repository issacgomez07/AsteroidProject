from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface = screen, color = "white", center = self.position, radius = self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            random_angle = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
            
            new_asteroid_1.velocity = new_velocity_1 * 1.2
            new_asteroid_2.velocity = new_velocity_2 * 1.2
