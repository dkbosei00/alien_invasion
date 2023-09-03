class Settings:
    '''Class for all the settings for the game'''
    
    def __init__(self):
        '''Initialize game setting'''

        # Game constraints settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly to the game should speed up
        self.speedup_scale = 1.1

        # Value alien score should increase by per level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialise settings we need to change during the game.'''
        self.alien_speed = 1.0
        self.bullet_speed = 3.0
        self.ship_speed = 1.5

        # Fleet direction: 1 represents right & -1 respresents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        '''Increase speed settings and alient point value'''
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)