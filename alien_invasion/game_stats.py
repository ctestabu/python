class GameStats():

    def __init__(self, ai_settings):
        # stats
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        # init changes
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = False
        self.score = 0
