class Settings():
    """A class to store all the Settings for Alien Invasion."""
    """Initialize the game's static settings"""
    def __init__(self):
        """initialize the game's Settings"""
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game spped up
        self.speed_up_scale = 1.2
        # How quickly the alien point values increse
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throught the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50


    def increse_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points *= self.score_scale
