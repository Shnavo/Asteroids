import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
asteroidfield = AsteroidField()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for object in asteroids:
            if object.collision_check(player):
                return print("Game Over!")
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # print(clock.tick(60))
    

# def main():
#     print(
#         f"Starting Asteroids!\n"
#         f"Screen width: {SCREEN_WIDTH}\n"
#         f"Screen height: {SCREEN_HEIGHT}"
#         )

if __name__ == "__main__":
    main()