import pygame


class GameCharacter:
    def __init__(self, image_path, screen):
        self.image = pygame.image.load(image_path)
        self.screen = screen

    def draw(self):
        # Get the width and height of the screen
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        # Get the width and height of the image
        image_width = self.image.get_width()
        image_height = self.image.get_height()

        # Calculate the position to draw the image at
        pos_x = (screen_width - image_width) // 2
        pos_y = (screen_height - image_height) // 2

        # Draw the image
        self.screen.blit(self.image, (pos_x, pos_y))


def run_game():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    # Create the game character
    character = GameCharacter("alien_invasion/images/alien.bmp", screen)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with a blue color
        screen.fill((0, 0, 255))

        # Draw the game character
        character.draw()

        # Update the display
        pygame.display.flip()


# Run the game
run_game()
