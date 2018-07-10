class GameStats():
    """Track statics for alien invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Intialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
