import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''This class is to create an alien object and its functionalities'''

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image for aliens
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each aliens starts with its own coordinates
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Convert int rect coordinate to temp float values
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edge(self):
        '''Return True when the screen edges are hit'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x