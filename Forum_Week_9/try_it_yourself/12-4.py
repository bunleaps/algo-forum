import pygame
import sys


def run_game():
    # Initialize Pygame and set up the display window.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
