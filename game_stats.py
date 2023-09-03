class GameStats:
    '''Class for managing the game's stats'''

    def __init__(self, ai_game) -> None:
        '''Initialize stats'''
        # Starts with an active agme
        self.game_active = True
        
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''Initialize stats thaat can change during the game'''

        self.ships_left = self.settings.ship_limit