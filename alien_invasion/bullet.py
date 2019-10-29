import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        # bullet create
        super(Bullet, self).__init__()
        # super().__init__
        self.screen = screen
        # bullet position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bullet positin
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # bullet tavel
        self.y -= self.speed_factor
        # rect refresh
        self.rect.y = self.y

    def draw_bullet(self):
        # bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
