import sys
import pygame

from ship import Ship
from bullet import Bullet
from settings import Settings
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.create_fleet()

    def run_game(self):
        '''Start the main loop in the game'''
        while True:
            self.check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        self.aliens.draw(self.screen)

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

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        # Delete both bullet and alien upon collision, True arguments mean thy will be deleted
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Repopulate fleet when all aliens are destroyed
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()

    def create_fleet(self):
        '''Create an alien fleet'''

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # Determine the number of aliens one row can have
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows for a fleet
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_aliens(alien_number, row)


    def _create_aliens(self, alien_number, number_of_rows):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * number_of_rows
        self.aliens.add(alien)

    def _update_aliens(self):
        '''Update the position of all the aliens'''
        self._check_fleet_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('BAM!')

    def _check_fleet_edge(self):
        # Respond if any fleet hits an edge
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        '''Drop the fleet and change the direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    # Run an instance of the game when the file is ran
    ai = AlienInvasion()
    ai.run_game()

