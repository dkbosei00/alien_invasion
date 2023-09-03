import sys
import pygame

from ship import Ship
from bullet import Bullet
from settings import Settings

class AlienInvasion:
    '''Overall class to manage game's behaviour'''

    def __init__(self):
        '''Initialize game'''

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.bg_color = (230, 230, 230)

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Start the main loop in the game'''
        while True:
            self.check_events()
            self.ship.update()

            self._update_bullets()
            self._update_screen()

    def check_events(self):
            '''To watch keyboard and mouse events'''
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _update_screen(self):
            '''Update images on the screen, and flip to the new screen.'''
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
             self.fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def fire_bullet(self):
         '''Create a new bullet and add it to the bullets group.'''
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update bullets within the game.'''
        self.bullets.update()

        # Get rid of disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        # print(len(self.bullets))


if __name__ == '__main__':
    # Run an instance of the game when the file is ran
    ai = AlienInvasion()
    ai.run_game()

