import pygame


def run_game():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with a blue color
        screen.fill((0, 0, 255))

        # Update the display
        pygame.display.flip()


# Run the game
run_game()
