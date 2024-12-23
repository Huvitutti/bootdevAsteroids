import pygame
from constants import *

print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:

    screen.fill((0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
    main()