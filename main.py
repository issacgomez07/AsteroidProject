import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable) # type: ignore
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable) # type: ignore

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill(color = "black")
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            for s in shots:
                if s.collisioncheck(a):
                    a.split()
            if player.collisioncheck(a):
                sys.exit("Game over!")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
