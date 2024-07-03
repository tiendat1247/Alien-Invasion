import pygame

class Ship:

    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("Image/ship.bmp")
        #Get the original size
        original_size = self.image.get_size()
        #Keep the ratio, lower the size to 1/4
        new_ship_size = [original_size[0]//4, original_size[1]//4]

        self.image = pygame.transform.scale(self.image, new_ship_size)

        self.rect = self.image.get_rect()

        # Center the ship on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)

