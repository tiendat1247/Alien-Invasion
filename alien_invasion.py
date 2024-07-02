#Create a Pygame window, create a class call AlienInvasion to represent the game
import sys
import pygame

from settings import Settings
from ship import Ship

class Alieninvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        # Set the background color
        self.bg_color = (230,230,230) 
        """Create game window"""
        pygame.display.set_caption("Alien Invasion")
        """Set caption for the window"""
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            """Watch for keyboard and mouse event"""
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    """Make the game Instances and run the game"""
    ai = Alieninvasion()
    ai.run_game()




