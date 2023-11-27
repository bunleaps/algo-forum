import sys
import pygame
from pygame.sprite import Sprite


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement speed
        self.speed = 1

    def draw(self):
        # Draw the rocket at its current location
        self.screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen.get_height():
            self.rect.y += self.speed


# Bullet inherit Sprite
class Bullet(Sprite):
    def __init__(self, screen, rocket):
        super().__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = rocket.rect.centery
        self.rect.left = rocket.rect.right

        # Store a decimal value for the bullet's position.
        self.x = float(self.rect.x)

        # Set the bullet's color
        self.color = (60, 60, 60)
        # Set the bullet's speed
        self.speed = 1.5

    def update(self):
        # Move the bullet up the screen
        self.rect.x += self.speed
        # Remove the bullet if it moves off the top of the screen
        if self.rect.left > self.screen.get_width():
            self.kill()

    def draw(self):
        # Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)


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
        rocket.draw_bullets()

        # Update the display
        pygame.display.flip()


# Run the game
run_game()
