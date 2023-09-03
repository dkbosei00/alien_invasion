import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    '''Class for ship functionality'''

    def __init__(self, ai_game) -> None:
        super().__init__()

        '''Initialize ship's position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # Load image and get ship's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship from the mid bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flag.'''

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''Draw ship at current location'''

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship to the bottom of the screen.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)