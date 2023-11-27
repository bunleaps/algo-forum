import sys
import pygame


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Movement speed
        self.speed = 1

    def draw(self):
        # Draw the rocket at its current location
        self.screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen.get_width():
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen.get_height():
            self.rect.y += self.speed


def run_game():
    # Initialize Pygame, settings, and screen object.
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Make a rocket.
    rocket = Rocket(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the screen with a blue color
        screen.fill((255, 255, 255))

        # Move and draw the rocket
        rocket.move()
        rocket.draw()

        # Update the display
        pygame.display.flip()


# Run the game
run_game()
