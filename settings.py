class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings.
        :rtype: object
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)

        self.ship_limit = 2
        self.alien_bullet_width = 5
        self.alien_bullet_height = 20
        self.alien_bullet_color = 255, 255, 0
        self.alien_bullets_every = 1.3

        self.ship_bullet_height = 30
        self.ship_bullet_width = 10
        self.ship_bullet_color = 65, 50, 85
        self.ship_bullets_every = 1

        self.fleet_drop_speed = 10
        self.debounce = 0.0001

        self.score_scale = 1
        self.alien_points = 1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 1
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 1
        self.speedup_scale = 1.1

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed_factor *= scale
        self.bullet_speed_factor *= scale
        self.alien_speed *= scale
        self.alien_points = int(self.alien_points * self.score_scale)
