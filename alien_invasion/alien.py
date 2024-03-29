import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 1 alien

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # image load
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # top lef spot
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # save alien pos
        self.x = float(self.rect.x)

    def blitme(self):
        # show alien
        self.screen.blit(self.image, self.rect)

    def update(self):
        # move alien
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # True if on the edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
