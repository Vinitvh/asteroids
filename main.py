import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid) == True:
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()
