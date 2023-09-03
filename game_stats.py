class GameStats:
    '''Class for managing the game's stats'''

    def __init__(self, ai_game) -> None:
        '''Initialize stats'''
        # Starts with an active agme
        self.game_active = False

        self.settings = ai_game.settings
        self.reset_stats()

        # High score
        self.high_score = 0

    def reset_stats(self):
        '''Initialize stats thaat can change during the game'''

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1