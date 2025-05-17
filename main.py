# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    # initialize the pygame module
    pygame.init()

    # use pygame's display.set_mode to get a new GUI window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Fill the screen with black (RGB: 0, 0, 0)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()


if __name__ == "__main__":
    main()
