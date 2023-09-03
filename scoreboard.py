import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    '''Class for scoreboard conditions and display'''

    def __init__(self, ai_game) -> None:
        '''Initializing scoreboard attributes'''

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self._prep_score()
        self._prep_high_score()
        self._prep_level()
        self._prep_ships()

    def _prep_score(self):
        '''Turn the score into rendered image'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score on top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Draw score to the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def _prep_high_score(self):
        '''Turn highscore into rendered image'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def check_high_score(self):
        '''Check high Score'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._prep_high_score()

    def _prep_level(self):
        '''Turn level into rendered image'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Positon level at the left top corner of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 50

    def _prep_ships(self):
        '''Turn ships left into a rendered image'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

