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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5