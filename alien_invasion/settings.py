class Settings():
    # Class for settings

    def __init__(self):
        # settings init
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship settings
        # self.ship_speed_factor = 25
        self.ship_limit = 3
        # bullet
        # self.bullet_speed_factor = 10
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10
        # alien
        # self.alien_speed_factor = 50
        self.fleet_drop_speed = 10
        # 1 -left -1 -right
        self.fleet_direction = 1
        # change settings
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale    

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
