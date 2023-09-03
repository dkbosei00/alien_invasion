class Settings:
    '''Class for all the settings for the game'''
    
    def __init__(self):
        '''Initialize game setting'''

        # Game constraints settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction: 1 represents right & -1 respresents left
        self.fleet_direction = 1