import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        player.update(dt)
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